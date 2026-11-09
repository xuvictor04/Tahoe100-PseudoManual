---
symbol: "PPP4R4"
type: "gene"
col: 4102
ensembl_id: "ENSG00000119698"
name: "protein phosphatase 4 regulatory subunit 4"
location: "14q32.2"
module: 14
arm: "+"
pooled_cpm: 25.9
n_lines_expressing: 40
n_dd_up: 35
n_dd_down: 17
n_dd_up_clean: 23
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PPP4R4

*protein phosphatase 4 regulatory subunit 4* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.87× (z +41.4, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.435× (z -10.2, q 1e-21, down in 18 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.636× (z -5.7, q 2e-06, down in 19 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL1A]] (+0.63, fdr 7e-06), [[PRKD3]] (+0.62, fdr 3e-05), [[STX11]] (+0.60, fdr 1e-05); moves opposite to [[NCBP3]] (-0.45, fdr 4e-05), [[VPS51]] (-0.42, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[CAMK4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.87×** | +41.4 | 0e+00 | 35/37 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.91×** | +19.6 | 0e+00 | 37/38 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.23×** | +18.4 | 0e+00 | 37/38 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.72×** | +16.8 | 0e+00 | 36/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.51×** | +16.0 | 0e+00 | 36/38 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +15.6 | 0e+00 | 34/38 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.13×** | +14.6 | 0e+00 | 36/38 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.63×** | +12.4 | 2e-33 | 32/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.20×** | +12.2 | 2e-32 | 30/39 (HOP62, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +11.4 | 3e-28 | 31/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.78×** | +10.4 | 8e-24 | 25/37 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +8.9 | 3e-17 | 25/37 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.76×** | +8.8 | 4e-17 | 34/38 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +6.6 | 2e-09 | 28/38 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.62×** | +5.9 | 1e-07 | 25/38 (A498, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.9 | 3e-05 | 17/38 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +4.7 | 7e-05 | 20/38 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 2e-04 | 16/38 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.85×** | +4.1 | 0.001 | 15/38 (CFPAC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -10.2 | 1e-21 | 18/26 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.467×** | -9.7 | 1e-19 | 26/35 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.636×** | -5.7 | 2e-06 | 19/38 (SW 900, Hs 766T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.495×** | -4.7 | 4e-04 | 17/37 (A549, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.705×** | -4.4 | 0.001 | 20/37 (SW 1271, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.603×** | -4.2 | 0.002 | 17/37 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -4.2 | 0.002 | 7/38 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.720×** | -4.2 | 0.002 | 15/38 (BT-474, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.715×** | -3.9 | 0.005 | 15/28 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.735×** | -3.9 | 0.005 | 17/38 (Panc 03.27, C32, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.742×** | -3.8 | 0.008 | 17/38 (NCI-H1573, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.009 | 17/38 (CFPAC-1, H4, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.749×** | -3.7 | 0.011 | 13/38 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.817×** | -3.6 | 0.012 | 14/38 (H4, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.050 | 13/38 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.694×** | -3.1 | 0.080 | 11/37 (SNU-1, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.789×** | -3.0 | 0.088 | 12/38 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.790×** | -3.0 | 0.088 | 11/38 (A-172, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 17.2 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +27.3) | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.2 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +26.7) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 6.59 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +20.3) | — |
| [[SW480 (line)]] | alt | 16.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +23.3) | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +23.0) | [[Selinexor (drug)]] 5 µM 0.275× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +20.1) | — |
| [[NCI-H1573 (line)]] | alt | 25.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 67.0× (z +27.9) | — |
| [[A549 (line)]] | wt | 14.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +20.5) | — |
| [[SNU-423 (line)]] | alt | 95.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.0658× (z -17.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 8.04 | 5 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 11.6× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 7.12 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +13.7) | — |
| [[A-172 (line)]] | wt | 45.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 59.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +21.7) | — |
| [[HS-578T (line)]] | alt | 16.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.5× (z +20.0) | — |
| [[J82 (line)]] | alt | 9.31 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.9× (z +19.8) | — |
| [[LOX-IMVI (line)]] | wt | 39.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 28.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.6) | — |
| [[RKO (line)]] | wt | 26.6 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.14× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -10.3) |
| [[SW 900 (line)]] | alt | 47.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +23.4) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 141 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0720× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.0× (z +21.2) | — |
| [[H4 (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 62.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 24.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +16.6) | — |
| [[SHP-77 (line)]] | alt | 89.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -13.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 75.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.6× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 61.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 46.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.114× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW 1088 (line)]] | alt | 50.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.8× (z +10.6) | — |
| [[A-427 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL1A]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PRKD3]] | +0.62 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[STX11]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TNFRSF1B]] | +0.59 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[MIR155HG]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SLCO5A1]] | +0.57 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SSTR2]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[IFNAR2]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[HMSD]] | +0.56 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[LRCH2]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[G0S2]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP3]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[VPS51]] | -0.42 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPP4R4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIK3CD]] | B | PIK3CD activity raises PPP4R4's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 3.71× lower at baseline in the lines without PIK3CD | 0.048 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[CAMK4]] | B | CAMK4 activity raises PPP4R4's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 2.63× lower at baseline in the lines without CAMK4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[CSRP2]] | B | CSRP2 activity raises PPP4R4's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 4.59× lower at baseline in the lines without CSRP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent; its own permutation p |
| [[SDK1]] | B | SDK1 activity raises PPP4R4's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without SDK1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[LRRC49]] | C | LRRC49 activity raises PPP4R4's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 3.67× lower at baseline in the lines without LRRC49 | 0.009 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent; co-absent with the target |
| [[CD83]] | C | CD83 activity raises PPP4R4's level | lines that do not express CD83 (4) vs lines expressing it (46) | 7.07× lower at baseline in the lines without CD83 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK4]] | B | PPP4R4 activity raises CAMK4's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 4.47× lower at baseline in the lines without PPP4R4 | 0.069 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[NKX3-1]] | B | PPP4R4 activity raises NKX3-1's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 2.61× lower at baseline in the lines without PPP4R4 | 0.072 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[TFB1M]] | B | PPP4R4 activity raises TFB1M's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without PPP4R4 | 0.073 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[ZNRF1]] | B | PPP4R4 activity raises ZNRF1's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without PPP4R4 | 0.092 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[LRRC49]] | C | PPP4R4 activity raises LRRC49's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 3.54× lower at baseline in the lines without PPP4R4 | 0.020 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 2.3); signed map (42.4, 13.1). **Vector** length 95.7, 23.9% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.1 | +12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.6 | +14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +19.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +41.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.9 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.3 | -4.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 4 regulatory subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:94,146,128-94,279,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP4R4, CFAP14; previously KIAA1622 |
| Gene groups (HGNC) | Protein phosphatase 4 regulatory subunits; Cilia and flagella associated; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUP7](https://www.uniprot.org/uniprotkb/Q6NUP7) (Serine/threonine-protein phosphatase 4 regulatory subunit 4):

> Putative regulatory subunit of serine/threonine-protein phosphatase 4.

**Summary**, from NCBI Gene [57718](https://www.ncbi.nlm.nih.gov/gene/57718):

> The protein encoded by this gene is a HEAT-like repeat-containing protein. The HEAT repeat is a tandemly repeated, 37-47 amino acid long module occurring in a number of cytoplasmic proteins. Arrays of HEAT repeats form a rod-like helical structure and appear to function as protein-protein interaction surfaces. The repeat-containing region of this protein has some similarity to the constant regulatory domain of the protein phosphatase 2A PR65/A subunit. The encoded protein binds protein …

**Accessions** — [HGNC:23788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23788) · Entrez [57718](https://www.ncbi.nlm.nih.gov/gene/57718) · UniProt [Q6NUP7](https://www.uniprot.org/uniprotkb/Q6NUP7) · Ensembl [ENSG00000119698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119698)

## Data

Gene col 4102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4102); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4102]; `tensor/DDL_lfc|DDL_z.npy` [4102]; `embed/gene_vectors.npy` [4102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4102 or target_col == 4102). Every well: [[PPP4R4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP4R4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
