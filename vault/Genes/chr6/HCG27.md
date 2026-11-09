---
symbol: "HCG27"
type: "gene"
col: 13042
ensembl_id: "ENSG00000206344"
name: "HLA complex group 27"
location: "6p21.33"
module: 35
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HCG27

*HLA complex group 27* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.11× (z +15.8, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.515× (z -6.5, q 4e-08, down in 20 of 45 measured lines) ⚠ unreliable plate only.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD14-DT]] (+0.74, fdr 7e-06), [[LINC01090]] (+0.73, fdr 7e-06), [[UPP2]] (+0.71, fdr 7e-06); moves opposite to [[POLR3B]] (-0.62, fdr 2e-05), [[PDHA1]] (-0.60, fdr 2e-05), [[HERC2]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +15.8 | 0e+00 | 32/34 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +10.3 | 3e-22 | 29/40 (HEC-1-A, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +9.4 | 5e-19 | 27/37 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +9.4 | 5e-19 | 2/9 (HT-29, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.6 | 3e-12 | 1/8 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.6 | 4e-09 | 14/30 (A498, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.7 | 1e-06 | 18/45 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.5 | 3e-06 | 10/46 (PANC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +5.3 | 7e-06 | 13/37 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +5.3 | 7e-06 | 14/31 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.1 | 2e-05 | 7/21 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.9 | 4e-05 | 7/45 (H4, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.5 | 3e-04 | 16/39 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.59×** | +4.4 | 4e-04 | 6/37 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 7/35 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.004 | 15/41 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.004 | 9/43 (LS 180, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.006 | 7/37 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.007 | 12/46 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.515×** | -6.5 | 4e-08 | 20/45 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.708× | -3.4 | 0.11 | 5/46 (KATO III, Hs 766T, …) | top dose only |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 0.705× | -3.3 | 0.11 | 9/36 (COLO 205, LS 180, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.706× | -3.3 | 0.11 | 10/39 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | 0.528× | -3.3 | 0.11 | 11/26 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +12.3) | — |
| [[A-172 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD14-DT]] | +0.74 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.73 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[UPP2]] | +0.71 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[HOXA-AS2]] | +0.70 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LINC02608]] | +0.69 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[BTG1-DT]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R42]] | +0.68 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LRRC8C-DT]] | +0.68 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[H2AZ1-DT]] | +0.67 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[UPK2]] | +0.66 | +0.58 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3B]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[PDHA1]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[HERC2]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RRP1B]] | -0.59 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[DNM1L]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NPM3]] | -0.57 | -0.51 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HCG27's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | HCG27's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | HCG27's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.56 | 0.520 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.2, 23.2); signed map (31.2, -1.1). **Vector** length 65.8, 10.8% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | HLA complex group 27 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.33 — chr6:31,197,760-31,203,968 (+) |
| Ensembl biotype | lncRNA |
| Also known as | bPG299F13.9, bCX101P6.9, bQB115I13.2, FLJ40123 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27366) · Entrez [253018](https://www.ncbi.nlm.nih.gov/gene/253018) · Ensembl [ENSG00000206344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206344)

## Data

Gene col 13042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13042); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13042]; `tensor/DDL_lfc|DDL_z.npy` [13042]; `embed/gene_vectors.npy` [13042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13042 or target_col == 13042). Every well: [[HCG27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCG27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
