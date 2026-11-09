---
symbol: "TRAF1"
type: "gene"
col: 638
ensembl_id: "ENSG00000056558"
name: "TNF receptor associated factor 1"
location: "9q33.2"
module: 112
arm: "+"
pooled_cpm: 17.71
n_lines_expressing: 38
n_dd_up: 30
n_dd_down: 31
n_dd_up_clean: 23
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 17
direction_downstream: 13
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# TRAF1

*TNF receptor associated factor 1* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 16.0× (z +45.9, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (1 with an alert ⚠); the strongest is [[Phenylephrine (hydrochloride) (drug)]] 5 µM: 0.587× (z -6.2, q 2e-07, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF2]] (+0.75, fdr 7e-06), [[IL1A]] (+0.75, fdr 7e-06), [[LIF]] (+0.75, fdr 7e-06); moves opposite to [[GLG1]] (-0.57, fdr 1e-05), [[NFATC3]] (-0.56, fdr 1e-05), [[ZDHHC7]] (-0.56, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[C15orf48]] → it (grade B ⚠); 13 go from it, the strongest it → [[MSANTD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **16.0×** | +45.9 | 0e+00 | 35/36 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **12.2×** | +28.1 | 0e+00 | 35/36 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.77×** | +26.7 | 0e+00 | 34/35 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.81×** | +15.7 | 0e+00 | 34/36 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.37×** | +10.1 | 5e-22 | 27/36 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.31×** | +9.8 | 1e-20 | 28/36 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.81×** | +8.2 | 2e-14 | 27/36 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.2 | 4e-11 | 19/32 (SW 900, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.68×** | +5.7 | 9e-07 | 17/35 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.58×** | +5.4 | 4e-06 | 20/36 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.58×** | +5.1 | 1e-05 | 20/36 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 2e-05 | 20/35 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM | ⚠ position correction uncertain | **1.34×** | +4.8 | 6e-05 | 18/36 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.8 | 8e-05 | 10/36 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 3e-04 | 17/36 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 5e-04 | 14/36 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.99×** | +4.2 | 7e-04 | 18/33 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.45×** | +4.2 | 7e-04 | 15/35 (PANC-1, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 1 with an alert ⚠; shown: the 15 strongest. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -6.2 | 2e-07 | 24/36 (NCI-H2347, A498, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.369×** | -6.1 | 2e-07 | 20/32 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.593×** | -6.1 | 2e-07 | 21/35 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -6.0 | 2e-07 | 20/36 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -5.9 | 4e-07 | 22/36 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.604×** | -5.9 | 4e-07 | 21/35 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.619×** | -5.4 | 7e-06 | 21/36 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -5.0 | 4e-05 | 15/36 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.651×** | -5.0 | 4e-05 | 20/35 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.637×** | -4.8 | 6e-05 | 20/35 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.659×** | -4.8 | 6e-05 | 18/36 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.664×** | -4.8 | 9e-05 | 20/36 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.666×** | -4.7 | 9e-05 | 20/36 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.666×** | -4.7 | 9e-05 | 17/36 (NCI-H1792, A498, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.669×** | -4.7 | 1e-04 | 18/36 (NCI-H1792, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +25.6) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[A549 (line)]] | wt | 52.9 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +23.2) | [[Clobetasol propionate (drug)]] 0.5 µM 0.252× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +17.0) | [[Adagrasib (drug)]] 0.05 µM 0.434× (z -15.0) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 33.1 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.9) | [[Clobetasol propionate (drug)]] 0.5 µM 0.142× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 9.32 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +20.9) | — |
| [[A-172 (line)]] | wt | 23.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.4× (z +25.5) | — |
| [[HS-578T (line)]] | alt | 22.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +20.7) | — |
| [[J82 (line)]] | alt | 37.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +26.6) | — |
| [[NCI-H23 (line)]] | alt | 63.5 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SNU-423 (line)]] | alt | 37.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 25.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +25.5) | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0388× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H2347 (line)]] | alt | 20.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +21.8) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.195× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 17.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 28.3× (z +21.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[PANC-1 (line)]] | alt | 18.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +25.1) | — |
| [[CFPAC-1 (line)]] | alt | 7.59 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.7× (z +19.9) | — |
| [[HEC-1-A (line)]] | alt | 5.14 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.2× (z +20.1) | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +15.1) | — |
| [[RKO (line)]] | wt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 71.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 16.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +19.2) | — |
| [[SW480 (line)]] | alt | 4.54 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +15.6) | — |
| [[C32 (line)]] | wt | 8.26 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +12.8) | [[Cobimetinib (drug)]] 5 µM 0.0700× (z -9.5) |
| [[H4 (line)]] | wt | 28.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +14.3) | — |
| [[Hs 766T (line)]] | wt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.1× (z +20.9) | — |
| [[SW48 (line)]] | wt | 6.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.4× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 5.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.1× (z +16.6) | — |
| [[HepG2_C3A (line)]] | wt | 6.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.0× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 5.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +12.1) | — |
| [[A-427 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF2]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[IL1A]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 485 |
| [[LIF]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[HDAC9]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[MSANTD3]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[CXCL8]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[ADORA2A]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PLAU]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[HMGN2P46]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SERPINB7]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[GATM]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PLA2G4C]] | +0.67 | +0.58 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLG1]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.56 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ZDHHC7]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CLASP1]] | -0.55 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | C15orf48 activity raises TRAF1's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 3.18× lower at baseline in the lines without C15orf48 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[HMGN2P46]] | B | HMGN2P46 activity raises TRAF1's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 3.34× lower at baseline in the lines without HMGN2P46 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[RUNX1]] | B | RUNX1 activity raises TRAF1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without RUNX1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[LRRC49]] | B | LRRC49 activity raises TRAF1's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without LRRC49 | 0.019 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[NKX3-1]] | B | NKX3-1 activity raises TRAF1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without NKX3-1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises TRAF1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.87× lower at baseline in the lines without ADTRP | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[ARNT2]] | B | ARNT2 activity raises TRAF1's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.31× lower at baseline in the lines without ARNT2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[TNFRSF9]] | B | TNFRSF9 activity raises TRAF1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without TNFRSF9 | 0.051 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[SRPX]] | B | SRPX activity raises TRAF1's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.40× lower at baseline in the lines without SRPX | 0.053 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[CCL5]] | B | CCL5 activity raises TRAF1's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 3.03× lower at baseline in the lines without CCL5 | 0.056 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[ROR1-AS1]] | B | ROR1-AS1 activity raises TRAF1's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without ROR1-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[NR3C1]] | B | NR3C1 activity lowers TRAF1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD3]] | B | TRAF1 activity raises MSANTD3's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without TRAF1 | 0.005 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[TMEFF1]] | B | TRAF1 activity raises TMEFF1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without TRAF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[CREB5]] | B | TRAF1 activity raises CREB5's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.80× lower at baseline in the lines without TRAF1 | 0.024 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[CLEC2D]] | B | TRAF1 activity raises CLEC2D's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without TRAF1 | 0.037 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[MMRN2]] | B | TRAF1 activity raises MMRN2's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TRAF1 | 0.040 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[CD83]] | B | TRAF1 activity raises CD83's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without TRAF1 | 0.044 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[SLCO5A1]] | B | TRAF1 activity raises SLCO5A1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without TRAF1 | 0.045 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[ADORA2A]] | B | TRAF1 activity raises ADORA2A's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without TRAF1 | 0.072 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[NINJ1]] | B | TRAF1 activity raises NINJ1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without TRAF1 | 0.073 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[DPF3]] | B | TRAF1 activity raises DPF3's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.22× lower at baseline in the lines without TRAF1 | 0.076 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[BHLHE40]] | B | TRAF1 activity raises BHLHE40's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without TRAF1 | 0.086 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[RUNX1]] | B | TRAF1 activity raises RUNX1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without TRAF1 | 0.088 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.858). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.2, 1.3); signed map (40.9, 12.0). **Vector** length 119, 34.4% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.70 to 5); *inflammatory response* (hallmark, mean cos +0.66 to 6); *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.68 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +28.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +45.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +26.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +9.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +1.5 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.3 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.0 | -4.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.8 | -4.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:120,902,393-120,929,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EBI6 |
| Gene groups (HGNC) | TNF receptor associated factors |
| Hallmark sets | KRAS_SIGNALING_UP, APICAL_JUNCTION, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling; TNF signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13077](https://www.uniprot.org/uniprotkb/Q13077) (TNF receptor-associated factor 1):

> Adapter molecule that is involved in multiple signaling pathways including the NF-kappa-B and MAPK pathways and thus influences inflammatory and apoptotic responses. Plays a critical role in regulating T-cell activation both through restricting the costimulation-independent activation of NIK in activated T-cells and by promoting the TNFRSF9-induced classical NF-kappa-B pathway (By similarity). Forms a heterotrimer with TRAF2 as part of an E3 ubiquitin-protein ligase complex that mediates …

**Summary**, from NCBI Gene [7185](https://www.ncbi.nlm.nih.gov/gene/7185):

> The protein encoded by this gene is a member of the TNF receptor (TNFR) associated factor (TRAF) protein family. TRAF proteins associate with, and mediate the signal transduction from various receptors of the TNFR superfamily. This protein and TRAF2 form a heterodimeric complex, which is required for TNF-alpha-mediated activation of MAPK8/JNK and NF-kappaB. The protein complex formed by this protein and TRAF2 also interacts with inhibitor-of-apoptosis proteins (IAPs), and thus mediates the …

**Accessions** — [HGNC:12031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12031) · Entrez [7185](https://www.ncbi.nlm.nih.gov/gene/7185) · UniProt [Q13077](https://www.uniprot.org/uniprotkb/Q13077) · Ensembl [ENSG00000056558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056558)

## Data

Gene col 638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 638); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 638]; `tensor/DDL_lfc|DDL_z.npy` [638]; `embed/gene_vectors.npy` [638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 638 or target_col == 638). Every well: [[TRAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
