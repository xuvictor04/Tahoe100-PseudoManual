---
symbol: "CHRNA5"
type: "gene"
col: 9836
ensembl_id: "ENSG00000169684"
name: "cholinergic receptor nicotinic alpha 5 subunit"
location: "15q25.1"
module: 60
arm: "+"
pooled_cpm: 9.32
n_lines_expressing: 49
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CHRNA5

*cholinergic receptor nicotinic alpha 5 subunit* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (22 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.75× (z +18.2, q 0e+00, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 3.14× (z +15.8, q 0e+00, up in 41 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HCT15 0.0751×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.197×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.115×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPE1]] (+0.69, fdr 7e-06), [[HSP90AA2P]] (+0.69, fdr 7e-06), [[TMEM97]] (+0.68, fdr 7e-06); moves opposite to [[ZZEF1]] (-0.56, fdr 1e-05), [[HARBI1]] (-0.56, fdr 5e-05), [[RSPRY1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **3.75×** | +18.2 | 0e+00 | 44/46 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **3.34×** | +16.6 | 0e+00 | 45/46 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.14×** | +15.8 | 0e+00 | 41/46 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **3.14×** | +15.8 | 0e+00 | 42/46 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.35×** | +15.1 | 0e+00 | 39/44 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.90×** | +14.7 | 0e+00 | 37/45 (C32, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.73×** | +13.8 | 1e-41 | 37/46 (A498, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.99×** | +13.4 | 4e-39 | 33/43 (A549, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **2.49×** | +12.6 | 2e-34 | 24/31 (LoVo, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.32×** | +11.6 | 2e-29 | 35/46 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **2.62×** | +11.0 | 3e-26 | 31/34 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.54×** | +10.6 | 1e-24 | 29/36 (SHP-77, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.10×** | +10.2 | 9e-23 | 28/31 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.76×** | +10.0 | 5e-22 | 31/46 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.97×** | +9.4 | 3e-19 | 28/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +8.9 | 2e-17 | 23/41 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.7 | 5e-13 | 27/46 (LoVo, SHP-77, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.8 | 2e-07 | 16/46 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +4.9 | 2e-05 | 12/45 (SW1417, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 8e-05 | 15/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 1e-04 | 13/47 (A-172, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +4.2 | 4e-04 | 8/38 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.75×** | +4.0 | 9e-04 | 7/35 (SHP-77, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.75×** | +4.0 | 1e-03 | 6/43 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9836.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HCT15 0.0751×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.197×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 0.847× | -3.3 | 0.53 | 8/46 (Hs 766T, HEC-1-A, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.804× | -3.1 | 0.53 | 3/46 (HEC-1-A, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.99 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.87 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.0× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 15.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 7.71 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.59× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SW1417 (line)]] | alt | 11.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 5.16 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.2× (z +9.2) | — |
| [[LoVo (line)]] | wt | 8.66 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[A-172 (line)]] | wt | 4.34 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.6× (z +8.7) | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -9.3) |
| [[A549 (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +10.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 5.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +9.3) | — |
| [[C32 (line)]] | wt | 3.60 | 1 | 0 | [[Auranofin (drug)]] 5 µM 26.3× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 11.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.12× (z +9.9) | — |
| [[J82 (line)]] | alt | 6.90 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.83× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 4.95 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.115× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 5.40 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.32× (z +9.8) | — |
| [[RKO (line)]] | wt | 12.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.32× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0613× (z -8.6) |
| [[SHP-77 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.42× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.23× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPE1]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TMEM97]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FABP5]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SORD]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[AHSA1]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RAB39A]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FKBP4]] | +0.61 | +0.69 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[NECAB3]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[C1orf216]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[DGKG]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZZEF1]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[HARBI1]] | -0.56 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[RSPRY1]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[METTL25B]] | -0.54 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[SMIM14]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZNF862]] | -0.52 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TNRC6C]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[CEP63]] | -0.51 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[LINC00174]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[LINC02340]] | -0.50 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[MMUT]] | -0.50 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHRNA5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.6, -10.7); signed map (-27.2, -30.6). **Vector** length 76.2, 15.3% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.51 to 5); *Folding of actin by CCT/TriC* (reactome, mean cos +0.50 to 4); *MYC targets v1* (hallmark, mean cos +0.54 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +14.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +13.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.6 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.5 | +15.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor nicotinic alpha 5 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,565,520-78,595,269 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cholinergic receptors nicotinic subunits |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 5 pathways, smallest: Acetylcholine binding and downstream events; Postsynaptic nicotinic acetylcholine receptors; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [P30532](https://www.uniprot.org/uniprotkb/P30532) (Neuronal acetylcholine receptor subunit alpha-5):

> Component of neuronal acetylcholine receptors (nAChRs) that function as pentameric, ligand-gated cation channels with high calcium permeability among other activities. nAChRs are excitatory neurotrasnmitter receptors formed by a collection of nAChR subunits known to mediate synaptic transmission in the nervous system and the neuromuscular junction. Each nAchR subunit confers differential attributes to channel properties, including activation, deactivation and desensitization kinetics, pH …

**Summary**, from NCBI Gene [1138](https://www.ncbi.nlm.nih.gov/gene/1138):

> The protein encoded by this gene is a nicotinic acetylcholine receptor subunit and a member of a superfamily of ligand-gated ion channels that mediate fast signal transmission at synapses. These receptors are thought to be heteropentamers composed of separate but similar subunits. Defects in this gene have been linked to susceptibility to lung cancer type 2 (LNCR2).[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:1959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1959) · Entrez [1138](https://www.ncbi.nlm.nih.gov/gene/1138) · UniProt [P30532](https://www.uniprot.org/uniprotkb/P30532) · Ensembl [ENSG00000169684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169684)

## Data

Gene col 9836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9836); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9836]; `tensor/DDL_lfc|DDL_z.npy` [9836]; `embed/gene_vectors.npy` [9836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9836 or target_col == 9836). Every well: [[CHRNA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRNA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
