---
symbol: "ADNP-AS1"
type: "gene"
col: 15200
ensembl_id: "ENSG00000259456"
name: "ADNP antisense RNA 1"
location: "20q13.13"
module: 21
arm: "+"
pooled_cpm: 3.54
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ADNP-AS1

*ADNP antisense RNA 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.65× (z +10.1, q 4e-21, up in 6 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +7.4, q 3e-11, up in 20 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Monocrotaline (drug)]] 5 µM in 1 line (J82 0.107×); [[Proglumide (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0584×); [[Vilanterol (drug)]] 0.5 µM in 1 line (PANC-1 0.149×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN7-AS1]] (+0.80, fdr 7e-06), [[CHMP3-AS1]] (+0.79, fdr 7e-06), [[CTDSPL2-DT]] (+0.77, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.1 | 4e-21 | 6/7 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +8.3 | 3e-14 | 14/22 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +8.3 | 3e-14 | 7/9 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.4 | 3e-11 | 20/36 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.8 | 9e-07 | 4/23 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.6 | 4e-04 | 10/33 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.5 | 5e-04 | 9/43 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.4 | 9e-04 | 10/23 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +4.0 | 0.004 | 10/36 (COLO 205, HS-578T, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.017 | 7/35 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.017 | 6/44 (PANC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.5 | 0.023 | 1/12 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.052 | 7/33 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.060 | 10/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.1 | 0.062 | 6/26 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.066 | 5/41 (C-33 A, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15200.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Monocrotaline (drug)]] 5 µM in 1 line (J82 0.107×); [[Proglumide (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0584×); [[Vilanterol (drug)]] 0.5 µM in 1 line (PANC-1 0.149×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -4.4 | 0.006 | 17/48 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.710× | -3.5 | 0.15 | 12/43 (SHP-77, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 2 | — | [[Proglumide (drug)]] 0.05 µM 0.0584× (z -9.9) |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.1000× (z -9.0) |
| [[HT-29 (line)]] | alt | 4.34 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.108× (z -8.8) |
| [[J82 (line)]] | alt | 5.89 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.107× (z -10.0) |
| [[PANC-1 (line)]] | alt | 2.94 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.149× (z -9.4) |
| [[SW1417 (line)]] | alt | 5.93 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0961× (z -9.3) |
| [[A-172 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN7-AS1]] | +0.80 | +0.72 / +0.73 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.79 | +0.75 / +0.72 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.77 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.75 | +0.62 / +0.72 | both halves | 7e-06 | same gene group |
| [[UBOX5-AS1]] | +0.75 | +0.60 / +0.76 | both halves | 7e-06 | same gene group |
| [[CNGB3]] | +0.75 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.74 | +0.64 / +0.69 | both halves | 7e-06 | same gene group |
| [[HRG-AS1]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 | same gene group |
| [[DNAJC9-AS1-1]] | +0.72 | +0.61 / +0.67 | both halves | 7e-06 | same gene group |
| [[RN7SL1]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 27.0); signed map (33.6, 4.0). **Vector** length 36.5, 3.28% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ADNP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.13 — chr20:50,930,984-50,945,148 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51227) · Entrez [101927631](https://www.ncbi.nlm.nih.gov/gene/101927631) · Ensembl [ENSG00000259456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259456)

## Data

Gene col 15200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15200); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15200]; `tensor/DDL_lfc|DDL_z.npy` [15200]; `embed/gene_vectors.npy` [15200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15200 or target_col == 15200). Every well: [[ADNP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADNP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
