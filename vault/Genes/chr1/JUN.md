---
symbol: "JUN"
type: "gene"
col: 10840
ensembl_id: "ENSG00000177606"
name: "Jun proto-oncogene, AP-1 transcription factor subunit"
location: "1p32.1"
module: 93
arm: "+"
pooled_cpm: 197.17
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# JUN

*Jun proto-oncogene, AP-1 transcription factor subunit* — 1p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 17.0× (z +39.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.517× (z -6.3, q 2e-07, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATF3]] (+0.74, fdr 7e-06), [[IQCN]] (+0.63, fdr 7e-06), [[CREB5]] (+0.62, fdr 1e-05); moves opposite to [[RNF4]] (-0.64, fdr 7e-06), [[MFSD14CP]] (-0.61, fdr 7e-06), [[ALG5]] (-0.61, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **17.0×** | +39.7 | 0e+00 | 48/48 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **11.9×** | +23.6 | 0e+00 | 48/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.98×** | +21.8 | 0e+00 | 48/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.02×** | +16.0 | 0e+00 | 47/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.67×** | +12.9 | 5e-36 | 48/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.46×** | +8.9 | 4e-17 | 44/48 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.38×** | +8.6 | 5e-16 | 43/49 (NCI-H460, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +8.3 | 8e-15 | 42/45 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.29×** | +8.2 | 1e-14 | 45/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.21×** | +7.9 | 2e-13 | 40/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.94×** | +6.3 | 1e-08 | 34/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +6.3 | 1e-08 | 40/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +6.0 | 1e-07 | 42/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.82×** | +6.0 | 1e-07 | 43/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.77×** | +5.7 | 5e-07 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.7 | 5e-07 | 43/48 (HS-578T, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.010 | 27/47 (C-33 A, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.010 | 34/49 (SHP-77, SNU-423, …) | all doses, flat |  |
| [[Gefitinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.012 | 29/48 (NCI-H460, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -6.3 | 2e-07 | 39/48 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.583×** | -5.3 | 3e-05 | 38/48 (HS-578T, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.610×** | -4.9 | 2e-04 | 33/48 (HOP62, A549, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.611×** | -4.9 | 2e-04 | 39/48 (NCI-H23, HCT15, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.650×** | -4.2 | 0.002 | 35/48 (A498, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.456×** | -4.1 | 0.005 | 40/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.766×** | -3.7 | 0.017 | 28/48 (C32, HT-29, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -3.5 | 0.030 | 30/49 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -3.4 | 0.041 | 30/50 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.078 | 27/48 (A549, A498, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.730× | -3.1 | 0.10 | 25/48 (HOP62, SW 900, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.733× | -3.1 | 0.10 | 26/48 (SW 900, SW 1088, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.736× | -3.0 | 0.11 | 27/48 (NCI-H460, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 139 | 17 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.8× (z +38.8) | — |
| [[SW48 (line)]] | wt | 126 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +25.7) | — |
| [[NCI-H1573 (line)]] | alt | 166 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +31.6) | — |
| [[A549 (line)]] | wt | 158 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +32.1) | — |
| [[AsPC-1 (line)]] | alt | 144 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +37.0) | — |
| [[CFPAC-1 (line)]] | alt | 307 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +37.1) | — |
| [[KATO III (line)]] | alt | 147 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +24.7) | — |
| [[SW1417 (line)]] | alt | 209 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +29.0) | — |
| [[SW480 (line)]] | alt | 186 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +25.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 97.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +35.6) | — |
| [[HOP62 (line)]] | alt | 249 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +32.3) | — |
| [[LOX-IMVI (line)]] | wt | 263 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +20.5) | — |
| [[NCI-H2347 (line)]] | alt | 165 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +35.2) | — |
| [[RKO (line)]] | wt | 331 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +19.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.6) |
| [[SNU-1 (line)]] | wt | 127 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +23.5) | — |
| [[C-33 A (line)]] | alt | 194 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +18.7) | — |
| [[HepG2_C3A (line)]] | wt | 253 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.7) |
| [[HS-578T (line)]] | alt | 242 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +36.1) | [[Ponatinib (drug)]] 5 µM 0.303× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 175 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 58.8× (z +40.6) | — |
| [[LS 180 (line)]] | wt | 201 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +26.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 338 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +27.8) | — |
| [[PANC-1 (line)]] | alt | 174 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +29.7) | — |
| [[A-172 (line)]] | wt | 203 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +31.6) | — |
| [[A-427 (line)]] | wt | 82.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +18.3) | — |
| [[J82 (line)]] | alt | 305 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +25.6) | — |
| [[SW 900 (line)]] | alt | 143 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +29.4) | — |
| [[A498 (line)]] | wt | 242 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.1× (z +37.9) | — |
| [[C32 (line)]] | wt | 228 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 64.0× (z +30.7) | [[Selinexor (drug)]] 5 µM 0.309× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 177 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +26.2) | — |
| [[NCI-H23 (line)]] | alt | 147 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +26.9) | [[Ponatinib (drug)]] 5 µM 0.264× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 191 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +25.3) | — |
| [[SK-MEL-2 (line)]] | alt | 79.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +23.0) | — |
| [[AN3 CA (line)]] | alt | 98.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 145 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 411 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +15.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 175 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +26.8) | — |
| [[Panc 03.27 (line)]] | alt | 165 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +27.0) | — |
| [[H4 (line)]] | wt | 245 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +20.8) | — |
| [[LoVo (line)]] | wt | 199 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +24.4) | — |
| [[SW 1088 (line)]] | alt | 233 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +19.9) | — |
| [[SW 1271 (line)]] | alt | 173 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +17.8) | — |
| [[BT-474 (line)]] | alt | 153 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +26.0) | — |
| [[COLO 205 (line)]] | alt | 406 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +22.3) | — |
| [[SNU-423 (line)]] | alt | 204 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +29.9) | — |
| [[HCT15 (line)]] | alt | 202 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +12.8) | — |
| [[CHP-212 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF3]] | +0.74 | +0.69 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 999 |
| [[IQCN]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CREB5]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 | STRING 971 |
| [[DUSP8]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: MAPK family signaling cascades; STRING 521 |
| [[JUND]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 | same gene group; pathway: Co-inhibition by PD-1; STRING 999 |
| [[IER2]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 681 |
| [[SQSTM1]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 589 |
| [[RHOB]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 519 |
| [[LINC02901]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SPTAN1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[DUSP10]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 | pathway: MAPK family signaling cascades; STRING 587 |
| [[CXCL8]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 987 |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[MFSD14CP]] | -0.61 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[ALG5]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[NUP54]] | -0.59 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[GTF3C2]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[PIK3R4]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 | pathway: Toll Like Receptor 9 (TLR9) Cascade |
| [[SNRNP40]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PARGP1]] | -0.57 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[MED17]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZDHHC7]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 | pathway: ESR-mediated signaling |
| [[CCT6P3-1]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises JUN's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PMAIP1]] | C | PMAIP1 activity weakens JUN's drug response | lines that do not express PMAIP1 (4) vs lines expressing it (45) | the lines without PMAIP1 respond 0.89× as strongly (z diff -2.27); strongest at Harringtonine 5 µM: 7.71x vs 11x (z diff -3.7) | 5e-04 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, 5.0); signed map (4.0, 20.6). **Vector** length 143, 57.6% of its response variance represented; |z| ≥ 3 in 1,660 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +23.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +3.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.5 | -0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.6 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.2 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.9 | -4.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Jun proto-oncogene, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.1 — chr1:58,776,845-58,784,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | c-Jun, AP-1 |
| Gene groups (HGNC) | Jun transcription factor family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, APOPTOSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 64 pathways, smallest: Activation of the AP-1 family of transcription factors; Killing mechanisms; WNT5:FZD7-mediated leishmania damping |
| Matched by | ensembl_id |

**Function**, from UniProt [P05412](https://www.uniprot.org/uniprotkb/P05412) (Transcription factor Jun):

> Transcription factor that recognizes and binds to the AP-1 consensus motif 5'-TGA[GC]TCA-3'. Heterodimerizes with proteins of the FOS family to form an AP-1 transcription complex, thereby enhancing its DNA binding activity to the AP-1 consensus sequence 5'-TGA[GC]TCA-3' and enhancing its transcriptional activity (By similarity). Together with FOSB, plays a role in activation-induced cell death of T cells by binding to the AP-1 promoter site of FASLG/CD95L, and inducing its transcription in …

**Summary**, from NCBI Gene [3725](https://www.ncbi.nlm.nih.gov/gene/3725):

> This gene is the putative transforming gene of avian sarcoma virus 17. It encodes a protein which is highly similar to the viral protein, and which interacts directly with specific target DNA sequences to regulate gene expression. This gene is intronless and is mapped to 1p32-p31, a chromosomal region involved in both translocations and deletions in human malignancies. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6204) · Entrez [3725](https://www.ncbi.nlm.nih.gov/gene/3725) · UniProt [P05412](https://www.uniprot.org/uniprotkb/P05412) · Ensembl [ENSG00000177606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177606)

## Data

Gene col 10840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10840); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10840]; `tensor/DDL_lfc|DDL_z.npy` [10840]; `embed/gene_vectors.npy` [10840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10840 or target_col == 10840). Every well: [[JUN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JUN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
