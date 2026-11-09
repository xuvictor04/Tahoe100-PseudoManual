---
symbol: "ANKRD33B"
type: "gene"
col: 8907
ensembl_id: "ENSG00000164236"
name: "ankyrin repeat domain 33B"
location: "5p15.2"
module: 14
arm: "+"
pooled_cpm: 103.82
n_lines_expressing: 35
n_dd_up: 33
n_dd_down: 17
n_dd_up_clean: 24
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 16
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ANKRD33B

*ankyrin repeat domain 33B* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.35× (z +42.1, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.618× (z -6.9, q 2e-09, down in 22 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belzutifan (drug)]] 5 µM: 0.490× (z -5.6, q 4e-06, down in 24 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K8]] (+0.70, fdr 7e-06), [[CSF1]] (+0.66, fdr 7e-06), [[TNFAIP2]] (+0.65, fdr 7e-06); moves opposite to [[TMED5]] (-0.51, fdr 1e-05), [[CLMP]] (-0.48, fdr 4e-05), [[UTP11]] (-0.47, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CAV1]] → it (grade B ⚠); 16 go from it, the strongest it → [[DRAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.35×** | +42.1 | 0e+00 | 33/33 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.93×** | +22.9 | 0e+00 | 33/33 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **12.0×** | +19.4 | 0e+00 | 33/34 (PANC-1, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.30×** | +17.8 | 0e+00 | 30/33 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.09×** | +11.0 | 6e-26 | 28/33 (HEC-1-A, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +10.8 | 4e-25 | 26/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +9.9 | 2e-21 | 20/34 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.5 | 1e-19 | 23/33 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +8.3 | 7e-15 | 23/33 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +7.7 | 7e-13 | 23/32 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.73×** | +7.5 | 4e-12 | 25/34 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.4 | 8e-12 | 26/33 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.7 | 7e-10 | 22/33 (NCI-H1792, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 2e-08 | 22/33 (A-427, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +5.6 | 1e-06 | 19/33 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.9 | 3e-05 | 18/33 (A-427, LOX-IMVI, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.6 | 1e-04 | 18/34 (NCI-H2030, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.4 | 3e-04 | 16/33 (CHP-212, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -6.9 | 2e-09 | 22/29 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.653×** | -6.4 | 5e-08 | 24/34 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.490×** | -5.6 | 4e-06 | 24/32 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -5.0 | 7e-05 | 22/33 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -4.4 | 0.002 | 19/33 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.005 | 10/33 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.754×** | -4.0 | 0.005 | 18/33 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.603×** | -4.0 | 0.005 | 18/33 (SW48, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.009 | 16/33 (LoVo, J82, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.617×** | -3.8 | 0.009 | 18/33 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.014 | 14/32 (SW48, LoVo, …) | two highest doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.015 | 13/34 (Hs 766T, C-33 A, …) | top dose only |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.023 | 11/34 (A-172, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.032 | 14/33 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.795×** | -3.2 | 0.061 | 8/33 (CHP-212, CFPAC-1, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.798×** | -3.1 | 0.069 | 7/34 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.819×** | -3.0 | 0.085 | 13/33 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.804×** | -3.0 | 0.085 | 11/34 (CFPAC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 68.4 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +27.9) | — |
| [[NCI-H460 (line)]] | wt | 112 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +16.3) | — |
| [[PANC-1 (line)]] | alt | 161 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +40.3) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 51.4 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +35.0) | — |
| [[A-172 (line)]] | wt | 148 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 215 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -16.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +27.5) | — |
| [[J82 (line)]] | alt | 319 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +31.7) | — |
| [[SW 900 (line)]] | alt | 66.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +23.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +28.8) | — |
| [[Panc 03.27 (line)]] | alt | 251 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +30.4) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -11.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 92.3 | 2 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 7.66× (z +11.9) | [[Bortezomib (drug)]] 0.05 µM 0.106× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.212× (z -9.4) |
| [[A-427 (line)]] | wt | 62.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +21.8) | — |
| [[A498 (line)]] | wt | 384 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 171 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +30.3) | — |
| [[CFPAC-1 (line)]] | alt | 63.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +30.7) | — |
| [[H4 (line)]] | wt | 68.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +20.4) | — |
| [[Hs 766T (line)]] | wt | 513 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -18.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 98.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 84.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 72.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +26.5) | — |
| [[HS-578T (line)]] | alt | 102 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +18.0) | — |
| [[AN3 CA (line)]] | alt | 117 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 77.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +21.5) | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -15.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 52.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +15.1) | — |
| [[SW 1271 (line)]] | alt | 129 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 54.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.7) | — |
| [[SW 1088 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 720 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K8]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[CSF1]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[IRF1]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[STAT5A]] | +0.61 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CD70]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NFKBIA]] | +0.60 | +0.56 / +0.64 | both halves | 1e-05 | same gene group |
| [[PTX3]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB10]] | +0.60 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[TNIP1]] | +0.58 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[SMAD7]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[FCHSD2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED5]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CLMP]] | -0.48 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[UTP11]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ARPC5L]] | -0.46 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[FAM120B]] | -0.46 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[HERC2P3]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[GPAT3]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[THBD]] | -0.45 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | CAV1 activity raises ANKRD33B's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 4.21× lower at baseline in the lines without CAV1 | 0.007 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[DRAM1]] | B | DRAM1 activity raises ANKRD33B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 5.36× lower at baseline in the lines without DRAM1 | 0.012 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[CSF1]] | C | CSF1 activity raises ANKRD33B's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 3.89× lower at baseline in the lines without CSF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1; co-absent with the target |
| [[CD83]] | C | CD83 activity raises ANKRD33B's level | lines that do not express CD83 (4) vs lines expressing it (46) | 8.07× lower at baseline in the lines without CD83 | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DRAM1]] | B | ANKRD33B activity raises DRAM1's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without ANKRD33B | 0.013 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[FAS]] | B | ANKRD33B activity raises FAS's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without ANKRD33B | 0.029 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[FAS]] | B | ANKRD33B activity strengthens FAS's drug response | lines that do not express ANKRD33B (10) vs lines expressing it (30) | the lines without ANKRD33B respond 0.61× as strongly (z diff +2.36); strongest at Homoharringtonine 5 µM: 1.21x vs 2.52x (z diff +5.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22; target measured in part of the lines; artifact flags |
| [[TMEM14C]] | B | ANKRD33B activity raises TMEM14C's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without ANKRD33B | 0.050 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[STX11]] | B | ANKRD33B activity raises STX11's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without ANKRD33B | 0.062 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[GRAMD1A]] | B | ANKRD33B activity raises GRAMD1A's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ANKRD33B | 0.062 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[EFNA1]] | B | ANKRD33B activity lowers EFNA1's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 2.16× higher at baseline in the lines without ANKRD33B | 0.063 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[LACTB]] | B | ANKRD33B activity raises LACTB's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without ANKRD33B | 0.067 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[NUAK1]] | B | ANKRD33B activity raises NUAK1's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without ANKRD33B | 0.080 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[ANO9]] | B | ANKRD33B activity lowers ANO9's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 2.59× higher at baseline in the lines without ANKRD33B | 0.080 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[BTN2A2]] | B | ANKRD33B activity raises BTN2A2's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without ANKRD33B | 0.084 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | ANKRD33B activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express ANKRD33B (15) vs lines expressing it (33) | the lines without ANKRD33B: 1.30× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 4.6); signed map (44.4, 7.3). **Vector** length 119, 37.7% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +22.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +19.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.4 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 33B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,564,070-10,657,816 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [A6NCL7](https://www.uniprot.org/uniprotkb/A6NCL7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35240) · Entrez [651746](https://www.ncbi.nlm.nih.gov/gene/651746) · UniProt [A6NCL7](https://www.uniprot.org/uniprotkb/A6NCL7) · Ensembl [ENSG00000164236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164236)

## Data

Gene col 8907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8907); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8907]; `tensor/DDL_lfc|DDL_z.npy` [8907]; `embed/gene_vectors.npy` [8907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8907 or target_col == 8907). Every well: [[ANKRD33B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD33B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
