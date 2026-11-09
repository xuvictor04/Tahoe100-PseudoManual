---
symbol: "DENND2B"
type: "gene"
col: 9307
ensembl_id: "ENSG00000166444"
name: "DENN domain containing 2B"
location: "11p15.4"
module: 14
arm: "+"
pooled_cpm: 44.71
n_lines_expressing: 44
n_dd_up: 39
n_dd_down: 16
n_dd_up_clean: 32
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# DENND2B

*DENN domain containing 2B* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +9.3, q 1e-17, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.579× (z -8.3, q 8e-14, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF1]] (+0.76, fdr 7e-06), [[TNFAIP2]] (+0.72, fdr 7e-06), [[STAT5A]] (+0.68, fdr 7e-06); moves opposite to [[SEPTIN10]] (-0.55, fdr 3e-05), [[ASL]] (-0.55, fdr 1e-04), [[WDR37]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLXDC2]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZNF775]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.3 | 1e-17 | 23/41 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +8.4 | 2e-14 | 28/42 (J82, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +7.1 | 2e-10 | 24/42 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +7.1 | 3e-10 | 26/41 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +7.0 | 4e-10 | 24/42 (MIA PaCa-2, A-172, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +6.9 | 6e-10 | 23/41 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +6.2 | 6e-08 | 23/42 (C32, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +5.9 | 3e-07 | 21/42 (NCI-H2347, J82, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +5.8 | 5e-07 | 20/42 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.7 | 6e-07 | 8/42 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 7e-07 | 23/42 (NCI-H2347, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +5.5 | 1e-06 | 23/41 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 7e-06 | 19/42 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +5.1 | 1e-05 | 20/42 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +5.0 | 2e-05 | 23/42 (NCI-H2347, BT-474, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +4.8 | 7e-05 | 19/42 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 16/42 (RPMI-7951, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.579×** | -8.3 | 8e-14 | 29/42 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -6.1 | 3e-07 | 20/30 (A498, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.671×** | -5.6 | 4e-06 | 21/33 (C-33 A, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.726×** | -4.9 | 2e-04 | 18/42 (SW480, SW1417, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.736×** | -4.6 | 4e-04 | 18/42 (C-33 A, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.768×** | -4.0 | 0.006 | 21/42 (SW480, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.772×** | -3.9 | 0.008 | 21/42 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.775×** | -3.7 | 0.014 | 15/41 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.785×** | -3.7 | 0.016 | 13/42 (BT-474, RPMI-7951, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.631×** | -3.6 | 0.016 | 11/41 (RPMI-7951, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.790×** | -3.6 | 0.018 | 14/41 (MIA PaCa-2, RPMI-7951, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.018 | 10/42 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.850× | -3.5 | 0.022 | 17/42 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.063 | 17/42 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.817×** | -3.1 | 0.084 | 9/42 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.684×** | -3.0 | 0.090 | 14/42 (PANC-1, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 81.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +20.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.9 | 4 (3 ⚠) | 4 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.19× (z +17.0) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 4.09× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.234× (z -9.2) |
| [[A498 (line)]] | wt | 275 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.264× (z -9.2) |
| [[PANC-1 (line)]] | alt | 54.3 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.87× (z +15.2) | — |
| [[SW480 (line)]] | alt | 58.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -10.4) |
| [[C-33 A (line)]] | alt | 49.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -12.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 44.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -11.8) |
| [[HT-29 (line)]] | alt | 58.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[J82 (line)]] | alt | 70.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +25.2) | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +20.6) | — |
| [[HCT15 (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 39.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.59× (z +10.0) | — |
| [[C32 (line)]] | wt | 50.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.33× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.21× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 43.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.52× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.1) | — |
| [[RKO (line)]] | wt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0827× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF1]] | +0.76 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[STAT5A]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CCL2]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TIFA]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[FAM111A-DT]] | +0.64 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.64 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CX3CL1]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[WTAP]] | +0.62 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CXCL3]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[OGFRL1]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN10]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ASL]] | -0.55 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[WDR37]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AP1M1]] | -0.53 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[GAN]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[LRRFIP1]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[DPP9]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PLA2G15]] | -0.52 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[ETV5]] | -0.52 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[MYO9B]] | -0.51 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[SKI]] | -0.51 | -0.45 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXDC2]] | B | PLXDC2 activity raises DENND2B's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without PLXDC2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF775]] | B | DENND2B activity raises ZNF775's level | lines that do not express DENND2B (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without DENND2B | 0.060 | ⚠ within organs, on part of the lines; also absent: POGLUT3, METRNL, MEX3A; maybe low, not absent |
| [[SEPTIN10]] | B | DENND2B activity lowers SEPTIN10's level | lines that do not express DENND2B (6) vs lines expressing it (44) | 1.79× higher at baseline in the lines without DENND2B | 0.067 | ⚠ within organs, on part of the lines; also absent: POGLUT3, METRNL, MEX3A; maybe low, not absent |
| [[ZNF470]] | B | DENND2B activity raises ZNF470's level | lines that do not express DENND2B (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without DENND2B | 0.085 | ⚠ within organs, on part of the lines; also absent: POGLUT3, METRNL, MEX3A; maybe low, not absent |
| [[RASGRP1]] | B | DENND2B activity lowers RASGRP1's level | lines that do not express DENND2B (6) vs lines expressing it (44) | 2.23× higher at baseline in the lines without DENND2B | 0.099 | ⚠ within organs, on part of the lines; also absent: POGLUT3, METRNL, MEX3A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, 4.6); signed map (44.2, 7.7). **Vector** length 108, 26.8% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +4.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -6.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,693,351-8,910,951 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HTS1, p126; previously ST5 |
| Gene groups (HGNC) | DENN domain containing |
| Hallmark sets | MYOGENESIS |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P78524](https://www.uniprot.org/uniprotkb/P78524) (DENN domain-containing protein 2B):

> [Isoform 1]: May be involved in cytoskeletal organization and tumorogenicity. Seems to be involved in a signaling transduction pathway leading to activation of MAPK1/ERK2. Plays a role in EGFR trafficking from recycling endosomes back to the cell membrane.; [Isoform 2]: Guanine nucleotide exchange factor (GEF) which may activate RAB9A and RAB9B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form.; [Isoform 3]: May block ERK2 …

**Summary**, from NCBI Gene [6764](https://www.ncbi.nlm.nih.gov/gene/6764):

> This gene was identified by its ability to suppress the tumorigenicity of Hela cells in nude mice. The protein encoded by this gene contains a C-terminal region that shares similarity with the Rab 3 family of small GTP binding proteins. This protein preferentially binds to the SH3 domain of c-Abl kinase, and acts as a regulator of MAPK1/ERK2 kinase, which may contribute to its ability to reduce the tumorigenic phenotype in cells. Three alternatively spliced transcript variants of this gene …

**Accessions** — [HGNC:11350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11350) · Entrez [6764](https://www.ncbi.nlm.nih.gov/gene/6764) · UniProt [P78524](https://www.uniprot.org/uniprotkb/P78524) · Ensembl [ENSG00000166444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166444)

## Data

Gene col 9307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9307); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9307]; `tensor/DDL_lfc|DDL_z.npy` [9307]; `embed/gene_vectors.npy` [9307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9307 or target_col == 9307). Every well: [[DENND2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
