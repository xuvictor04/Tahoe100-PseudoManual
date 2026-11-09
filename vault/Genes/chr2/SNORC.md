---
symbol: "SNORC"
type: "gene"
col: 11306
ensembl_id: "ENSG00000182600"
name: "secondary ossification center associated regulator of chondrocyte maturation"
location: "2q37.1"
module: null
arm: null
pooled_cpm: 14.24
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: false
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# SNORC

*secondary ossification center associated regulator of chondrocyte maturation* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +9.8, q 9e-20, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.508× (z -10.0, q 8e-21, down in 23 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.420× (z -7.0, q 6e-10, down in 30 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +9.8 | 9e-20 | 30/45 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.7 | 3e-12 | 28/46 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.4 | 2e-08 | 22/47 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.1 | 4e-05 | 17/48 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.9 | 9e-05 | 20/48 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 4e-04 | 17/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.32×** | +4.3 | 0.001 | 16/46 (LS 180, SW480, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 16/47 (NCI-H23, HT-29, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 16/47 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.004 | 11/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.10 | 9/47 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -10.0 | 8e-21 | 23/41 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -7.8 | 2e-12 | 26/43 (SW48, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -7.0 | 6e-10 | 30/48 (PANC-1, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -6.4 | 3e-08 | 24/44 (NCI-H460, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.652×** | -6.1 | 1e-07 | 19/32 (NCI-H1573, Hs 766T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.701×** | -5.5 | 5e-06 | 21/36 (NCI-H1573, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.720×** | -5.0 | 4e-05 | 21/46 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.730×** | -4.6 | 2e-04 | 18/47 (H4, A-427, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -4.4 | 6e-04 | 16/47 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.774×** | -3.9 | 0.005 | 17/47 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.780×** | -3.8 | 0.007 | 20/48 (PANC-1, SW48, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.023 | 6/47 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.787×** | -3.5 | 0.023 | 11/46 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.066 | 12/47 (BT-474, C-33 A, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.815×** | -3.1 | 0.066 | 3/48 (SW480, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.5 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.8) |
| [[BT-474 (line)]] | alt | 9.47 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.0969× (z -9.5) |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0555× (z -14.3) ⚠ toxic · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0970× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.3) ⚠ cell-cycle shift, explains ~66% of this change |
| [[AsPC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[LoVo (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.193× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.7) | — |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNORC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | secondary ossification center associated regulator of chondrocyte maturation |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:232,857,270-232,878,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ830, ASCL830; previously C2orf82 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX34](https://www.uniprot.org/uniprotkb/Q6UX34) (Protein SNORC):

> Plays a role in the regulation of chondrocyte maturation and postnatal endochondral ossification. May inhibit cell growth stimulation induced by FGF2.

**Summary**, from NCBI Gene [389084](https://www.ncbi.nlm.nih.gov/gene/389084):

> Predicted to be involved in cartilage development. Predicted to be located in cytoplasm and membrane. Predicted to be active in cell periphery. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33763) · Entrez [389084](https://www.ncbi.nlm.nih.gov/gene/389084) · UniProt [Q6UX34](https://www.uniprot.org/uniprotkb/Q6UX34) · Ensembl [ENSG00000182600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182600)

## Data

Gene col 11306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11306); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11306, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11306]; `tensor/DDL_lfc|DDL_z.npy` [11306]; `embed/gene_vectors.npy` [11306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11306 or target_col == 11306). Every well: [[SNORC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNORC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
