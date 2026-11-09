---
symbol: "RPL10A"
type: "gene"
col: 12668
ensembl_id: "ENSG00000198755"
name: "ribosomal protein L10a"
location: "6p21.31"
module: 43
arm: "+"
pooled_cpm: 186.65
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL10A

*ribosomal protein L10a* — 6p21.31

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +7.1, q 9e-10, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.42×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.27×; ⚠ cell-cycle shift, explains ~18% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.431×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS8]] (+0.89, fdr 7e-06), [[RPL7A]] (+0.88, fdr 7e-06), [[RPL13]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[EEF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12668.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.42×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.27×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.89×** | +7.1 | 9e-10 | 48/49 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.40×** | +5.7 | 4e-06 | 40/44 (NCI-H460, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.83×** | +4.7 | 6e-04 | 46/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.89×** | +4.5 | 8e-04 | 40/45 (A549, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.9 | 0.010 | 41/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12668.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.431×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.720× | -3.5 | 0.24 | 30/48 (Hs 766T, J82, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 187 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.5) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[NCI-H460 (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 195 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 160 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 256 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 142 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 193 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 322 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 270 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 287 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 294 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 229 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS8]] | +0.89 | +0.80 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7A]] | +0.88 | +0.77 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.88 | +0.76 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RACK1]] | +0.88 | +0.73 / +0.90 | both halves | 7e-06 | STRING 999 |
| [[RPL12]] | +0.87 | +0.78 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.87 | +0.75 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL15]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.87 | +0.77 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.87 | +0.77 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.87 | +0.74 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.86 | +0.75 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.86 | +0.76 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL7]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.86 | +0.72 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.86 | +0.71 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF2]] | C | RPL10A's natural level weakens EEF2's drug response | RPL10A's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.03; direction clear | 0.092 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.889). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.3, -28.6); signed map (-61.1, -5.0). **Vector** length 75.1, 41.4% of its response variance represented; |z| ≥ 3 in 421 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.75 to 19); *Translation initiation complex formation* (reactome, mean cos +0.73 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.73 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.0 | -0.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.6 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -4.6 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.4 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L10a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,468,401-35,470,785 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Csa-19, L10A, uL1; previously NEDD6 |
| Gene groups (HGNC) | L ribosomal proteins; MicroRNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62906](https://www.uniprot.org/uniprotkb/P62906) (Large ribosomal subunit protein uL1):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [4736](https://www.ncbi.nlm.nih.gov/gene/4736):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L1P family of ribosomal proteins. It is located in the cytoplasm. The expression of this gene is downregulated in the thymus by cyclosporin-A (CsA), an immunosuppressive …

**Accessions** — [HGNC:10299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10299) · Entrez [4736](https://www.ncbi.nlm.nih.gov/gene/4736) · UniProt [P62906](https://www.uniprot.org/uniprotkb/P62906) · Ensembl [ENSG00000198755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198755)

## Data

Gene col 12668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12668); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12668]; `tensor/DDL_lfc|DDL_z.npy` [12668]; `embed/gene_vectors.npy` [12668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12668 or target_col == 12668). Every well: [[RPL10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
