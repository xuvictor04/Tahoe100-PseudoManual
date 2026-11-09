---
symbol: "MSTO1"
type: "gene"
col: 4620
ensembl_id: "ENSG00000125459"
name: "misato mitochondrial distribution and morphology regulator 1"
location: "1q22"
module: 23
arm: "+"
pooled_cpm: 18.12
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MSTO1

*misato mitochondrial distribution and morphology regulator 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.01× (z +33.8, q 0e+00, up in 45 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.102×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.122×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213-AS1]] (+0.80, fdr 7e-06), [[C8orf44-SGK3]] (+0.76, fdr 7e-06), [[TBCE-1]] (+0.76, fdr 7e-06); moves opposite to [[ISCA2]] (-0.67, fdr 3e-04), [[MRPL17]] (-0.60, fdr 8e-05), [[THEM6]] (-0.60, fdr 5e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.01×** | +33.8 | 0e+00 | 45/46 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.06×** | +25.7 | 0e+00 | 30/30 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.28×** | +24.9 | 0e+00 | 42/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.98×** | +23.8 | 0e+00 | 39/40 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.33×** | +20.1 | 0e+00 | 34/35 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +14.9 | 0e+00 | 39/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.98×** | +14.3 | 2e-44 | 38/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +13.0 | 7e-37 | 35/42 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.35×** | +12.6 | 8e-35 | 42/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +12.4 | 2e-33 | 42/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +11.0 | 1e-26 | 36/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +10.5 | 5e-24 | 32/47 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +10.4 | 7e-24 | 32/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +10.1 | 2e-22 | 41/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +8.8 | 6e-17 | 34/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.8 | 4e-05 | 23/47 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 2e-04 | 17/46 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.2 | 6e-04 | 13/48 (PANC-1, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.72×** | +4.2 | 7e-04 | 12/45 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4620.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.102×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.778× | -3.5 | 0.23 | 9/48 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.5 | 9 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +17.9) | — |
| [[HOP62 (line)]] | alt | 12.0 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.89× (z +19.4) | — |
| [[SW 900 (line)]] | alt | 21.8 | 8 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +17.0) | — |
| [[SW480 (line)]] | alt | 22.8 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.8) | — |
| [[A-172 (line)]] | wt | 19.3 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +19.1) | — |
| [[A498 (line)]] | wt | 25.7 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.13× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.3) | — |
| [[LoVo (line)]] | wt | 19.3 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.4× (z +20.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 6 (3 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.18× (z +14.7) | — |
| [[Hs 766T (line)]] | wt | 14.7 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 14.4 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 29.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +22.4) | — |
| [[A549 (line)]] | wt | 11.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +15.9) | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +14.7) | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +9.9) | [[Canagliflozin (drug)]] 0.05 µM 0.102× (z -9.6) |
| [[J82 (line)]] | alt | 11.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.4× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +13.7) | — |
| [[KATO III (line)]] | alt | 15.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.59× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 6.73 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +17.4) | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.8× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 28.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.1× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +16.3) | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.2× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +13.0) | — |
| [[H4 (line)]] | wt | 12.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.7× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 22.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +12.5) | — |
| [[C32 (line)]] | wt | 11.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.34× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +17.3) | — |
| [[HCT15 (line)]] | alt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 11.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +15.4) | — |
| [[BT-474 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.1) | — |
| [[RKO (line)]] | wt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 7.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +14.5) | — |
| [[SW48 (line)]] | wt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +9.8) | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213-AS1]] | +0.80 | +0.82 / +0.61 | both halves | 7e-06 |  |
| [[C8orf44-SGK3]] | +0.76 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.76 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ZNF596]] | +0.76 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.75 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[GTF3C2-AS2]] | +0.73 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.73 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[SPTY2D1OS]] | +0.71 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.71 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[TAS2R4]] | +0.71 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[CDKL3]] | +0.70 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.69 | +0.74 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.67 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[MRPL17]] | -0.60 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[THEM6]] | -0.60 | -0.23 / -0.43 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MSTO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RGS2]] | B | RGS2 activity lowers MSTO1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.05× higher at baseline in the lines without RGS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-5.6, 22.7); signed map (30.9, -16.0). **Vector** length 82.0, 18.5% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +20.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +23.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +25.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +14.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +4.2 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.0 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | +8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | +12.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +2.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | misato mitochondrial distribution and morphology regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,563,235-155,614,951 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10504, LST005, MST, misato |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUK6](https://www.uniprot.org/uniprotkb/Q9BUK6) (Protein misato homolog 1):

> Involved in the regulation of mitochondrial distribution and morphology. Required for mitochondrial fusion and mitochondrial network formation.

**Summary**, from NCBI Gene [55154](https://www.ncbi.nlm.nih.gov/gene/55154):

> Involved in mitochondrion distribution; mitochondrion organization; and positive regulation of mitochondrial fusion. Located in mitochondrial outer membrane. Is active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29678) · Entrez [55154](https://www.ncbi.nlm.nih.gov/gene/55154) · UniProt [Q9BUK6](https://www.uniprot.org/uniprotkb/Q9BUK6) · Ensembl [ENSG00000125459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125459)

## Data

Gene col 4620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4620); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4620]; `tensor/DDL_lfc|DDL_z.npy` [4620]; `embed/gene_vectors.npy` [4620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4620 or target_col == 4620). Every well: [[MSTO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSTO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
