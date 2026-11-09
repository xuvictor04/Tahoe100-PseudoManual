---
symbol: "AP5M1"
type: "gene"
col: 597
ensembl_id: "ENSG00000053770"
name: "adaptor related protein complex 5 subunit mu 1"
location: "14q22.3"
module: 135
arm: "+"
pooled_cpm: 19.12
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# AP5M1

*adaptor related protein complex 5 subunit mu 1* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.09× (z +18.0, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.704× (z -6.1, q 6e-07, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0876×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.372×; ⚠ cell-cycle shift, explains ~16% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.392×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.439×).
> Its strongest partners by |cos| (56 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 44 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJB14]] (+0.74, fdr 1e-05), [[PBLD]] (+0.71, fdr 7e-04), [[MMADHC-DT]] (+0.69, fdr 0.002, ⚠ one half only (not replicated)), [[MAIP1]] (+0.69, fdr 8e-05); moves opposite to [[DNAAF3]] (-0.68, fdr 3e-04), [[KCTD17]] (-0.66, fdr 0.001, ⚠ one half only (not replicated)), [[MAST3]] (-0.65, fdr 0.003, ⚠ one half only (not replicated)), [[BAIAP3]] (-0.65, fdr 1e-04), [[RHPN1]] (-0.64, fdr 6e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +18.0 | 0e+00 | 41/46 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +11.1 | 5e-26 | 35/48 (SW1417, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +10.1 | 1e-21 | 35/43 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +9.7 | 3e-20 | 36/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +8.3 | 1e-14 | 30/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +8.0 | 1e-13 | 27/48 (SNU-423, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.6 | 2e-12 | 29/47 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +7.3 | 2e-11 | 26/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.9 | 2e-10 | 17/32 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +6.6 | 2e-09 | 29/47 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +6.4 | 6e-09 | 26/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +6.1 | 6e-08 | 24/48 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.0 | 6e-08 | 24/48 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.0 | 6e-08 | 18/43 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 2e-07 | 28/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 2e-07 | 23/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +5.6 | 6e-07 | 23/48 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.7 | 8e-05 | 19/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 597.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0876×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.372×; ⚠ cell-cycle shift, explains ~16% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.392×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.439×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -6.1 | 6e-07 | 24/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.768×** | -4.6 | 0.001 | 18/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.824× | -3.4 | 0.14 | 15/47 (SW480, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | 0.836× | -3.1 | 0.24 | 13/44 (HOP62, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Tetracycline (hydrochloride) (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.27 | 7/47 (A-172, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 15.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +11.6) | — |
| [[SW480 (line)]] | alt | 28.6 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.372× (z -10.5) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.392× (z -10.0) |
| [[LS 180 (line)]] | wt | 30.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.47× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 22.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 12.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +18.5) | — |
| [[SW1417 (line)]] | alt | 16.4 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.60× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0876× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +10.4) | — |
| [[RKO (line)]] | wt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.8) | — |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 33 of them with an alert (⚠; 33 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB14]] | +0.74 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PBLD]] | +0.71 | +0.57 / +0.21 | both halves | 7e-04 |  |
| [[MMADHC-DT]] | +0.69 | +0.63 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[MAIP1]] | +0.69 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[FBXO30]] | +0.69 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[WDR33]] | +0.68 | +0.62 / +0.24 | both halves | 5e-04 |  |
| [[PNISR-AS1]] | +0.67 | +0.50 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[MIER3]] | +0.67 | +0.63 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RNF6]] | +0.67 | +0.68 / +0.33 | both halves | 1e-04 |  |
| [[ZNF189]] | +0.66 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[PSMC2]] | +0.66 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[BAG2]] | +0.66 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[HTATIP2]] | +0.66 | +0.67 / +0.27 | both halves | 3e-04 |  |
| [[VPS52]] | +0.66 | +0.42 / +0.33 | both halves | 1e-04 |  |
| [[CLHC1]] | +0.64 | +0.62 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.68 | -0.49 / -0.26 | both halves | 3e-04 |  |
| [[KCTD17]] | -0.66 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[MAST3]] | -0.65 | -0.57 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[BAIAP3]] | -0.65 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.64 | -0.49 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[YIF1B]] | -0.64 | -0.55 / +0.03 | ⚠ one half (not replicated) | 1.00 |  |
| [[RHPN1]] | -0.64 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[DHTKD1]] | -0.64 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[FCHO1]] | -0.64 | -0.58 / +0.05 | ⚠ one half (not replicated) | 1.00 |  |
| [[NPHP4]] | -0.64 | -0.59 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[KLHL26]] | -0.63 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[TMEM256]] | -0.62 | -0.54 / -0.26 | both halves | 3e-04 |  |
| [[AFMID]] | -0.62 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[CARHSP1]] | -0.61 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[SLC2A3]] | -0.60 | -0.56 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AP5M1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HFE]] | B | HFE activity lowers AP5M1's level | lines that do not express HFE (5) vs lines expressing it (45) | 1.36× higher at baseline in the lines without HFE | 0.067 | ⚠ within organs, on part of the lines; also absent: HOXA-AS2, PIM1, CBR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-2.5, 12.6); signed map (20.9, -25.0). **Vector** length 95.8, 20.5% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +1.9 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.6 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.5 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -7.1 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +1.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 5 subunit mu 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:57,268,924-57,298,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10813, MuD, mu5; previously C14orf108, MUDENG |
| Gene groups (HGNC) | Adaptor related protein complex 5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0R1](https://www.uniprot.org/uniprotkb/Q9H0R1) (AP-5 complex subunit mu-1):

> As part of AP-5, a probable fifth adaptor protein complex it may be involved in endosomal transport. According to PubMed:18395520, it may play a role in cell death.

**Summary**, from NCBI Gene [55745](https://www.ncbi.nlm.nih.gov/gene/55745):

> Involved in endosomal transport. Located in several cellular components, including cytosol; late endosome; and lysosome. Part of AP-type membrane coat adaptor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20192) · Entrez [55745](https://www.ncbi.nlm.nih.gov/gene/55745) · UniProt [Q9H0R1](https://www.uniprot.org/uniprotkb/Q9H0R1) · Ensembl [ENSG00000053770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053770)

## Data

Gene col 597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 597); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 597]; `tensor/DDL_lfc|DDL_z.npy` [597]; `embed/gene_vectors.npy` [597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 597 or target_col == 597). Every well: [[AP5M1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP5M1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
