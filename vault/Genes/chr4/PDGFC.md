---
symbol: "PDGFC"
type: "gene"
col: 6993
ensembl_id: "ENSG00000145431"
name: "platelet derived growth factor C"
location: "4q32.1"
module: 121
arm: "+"
pooled_cpm: 131.01
n_lines_expressing: 37
n_dd_up: 6
n_dd_down: 33
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# PDGFC

*platelet derived growth factor C* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.08× (z +5.3, q 8e-05, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.338× (z -22.0, q 0e+00, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR3C1]] (+0.54, fdr 1e-05), [[ZFHX4]] (+0.54, fdr 3e-05), [[MIR3171HG]] (+0.52, fdr 3e-05); moves opposite to [[PPP1R32]] (-0.44, fdr 2e-04), [[GAN]] (-0.43, fdr 4e-05), [[ARMC10]] (-0.43, fdr 1e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MICU3]] → it (grade B ⚠); 3 go from it, the strongest it → [[RPGR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +5.3 | 8e-05 | 23/36 (PANC-1, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +5.0 | 2e-04 | 25/35 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +4.2 | 0.004 | 22/37 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.009 | 22/34 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.041 | 22/35 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.041 | 21/34 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.19× | +3.5 | 0.042 | 12/35 (A498, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.25× | +3.0 | 0.17 | 17/36 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.338×** | -22.0 | 0e+00 | 35/36 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.239×** | -20.5 | 0e+00 | 35/35 (SNU-1, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.244×** | -20.2 | 0e+00 | 35/35 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.362×** | -14.6 | 0e+00 | 35/35 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.375×** | -13.5 | 1e-39 | 31/33 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.383×** | -13.2 | 6e-38 | 32/37 (SNU-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.447×** | -11.3 | 2e-27 | 32/36 (SNU-1, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.472×** | -10.8 | 3e-25 | 33/35 (SNU-1, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.470×** | -10.4 | 1e-23 | 32/35 (HOP62, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.480×** | -10.1 | 3e-22 | 30/34 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.667×** | -8.2 | 9e-15 | 22/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.590×** | -7.0 | 1e-10 | 28/33 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.640×** | -6.4 | 7e-09 | 26/35 (HEC-1-A, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.640×** | -6.1 | 3e-08 | 27/34 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -5.7 | 4e-07 | 26/35 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -5.6 | 9e-07 | 25/35 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -5.5 | 1e-06 | 29/35 (SW 1088, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.700×** | -5.1 | 8e-06 | 21/35 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.723×** | -4.7 | 9e-05 | 20/35 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.568×** | -4.1 | 0.001 | 24/35 (PANC-1, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.001 | 22/36 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.782×** | -3.4 | 0.016 | 16/35 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.016 | 17/35 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -3.3 | 0.023 | 16/35 (HOP62, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 279 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -21.3) |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -16.5) |
| [[SW 900 (line)]] | alt | 203 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -21.8) |
| [[HEC-1-A (line)]] | alt | 285 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -22.3) |
| [[HOP62 (line)]] | alt | 192 | 2 (1 ⚠) | 10 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.38× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -22.1) |
| [[SNU-1 (line)]] | wt | 965 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0715× (z -28.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.116× (z -23.0) |
| [[SNU-423 (line)]] | alt | 206 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -21.9) |
| [[NCI-H1573 (line)]] | alt | 170 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -24.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -20.0) |
| [[A-427 (line)]] | wt | 779 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0834× (z -27.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.125× (z -23.4) |
| [[AN3 CA (line)]] | alt | 634 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0655× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 155 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -15.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.3) |
| [[LS 180 (line)]] | wt | 133 | 2 | 6 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.08× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.143× (z -18.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.165× (z -17.1) |
| [[PANC-1 (line)]] | alt | 83.0 | 2 (1 ⚠) | 6 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.19× (z +9.0) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 4.37× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -19.1) |
| [[HS-578T (line)]] | alt | 114 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -19.9) |
| [[HT-29 (line)]] | alt | 96.6 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 192 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.2) |
| [[A-172 (line)]] | wt | 86.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -12.2) |
| [[A498 (line)]] | wt | 137 | 1 (1 ⚠) | 5 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.40× (z +9.6) ⚠ unreliable plate only | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -17.5) |
| [[H4 (line)]] | wt | 114 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -9.4) |
| [[BT-474 (line)]] | alt | 43.0 | 4 (1 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.85× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.225× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 161 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -18.4) |
| [[NCI-H661 (line)]] | alt | 585 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -15.4) |
| [[Hs 766T (line)]] | wt | 67.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -13.4) |
| [[LoVo (line)]] | wt | 56.4 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.71× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.289× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 84.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.212× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -16.8) |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.7) |
| [[J82 (line)]] | alt | 75.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.5) |
| [[SW 1088 (line)]] | alt | 201 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0528× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -10.4) |
| [[CHP-212 (line)]] | wt | 116 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 69.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -10.3) |
| [[SW 1271 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0973× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 28.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.90 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR3C1]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ZFHX4]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[MIR3171HG]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ITGBL1]] | +0.52 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TRIO]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[MSC]] | +0.51 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[RBMS3]] | +0.51 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SYTL2]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ZEB2]] | +0.50 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CPED1]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SEMA3C]] | +0.50 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[IGSF1]] | +0.49 | +0.36 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R32]] | -0.44 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[GAN]] | -0.43 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ARMC10]] | -0.43 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CEACAM1]] | -0.43 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[TMEM181]] | -0.42 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[RPGR]] | -0.41 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[RAPGEF3]] | -0.41 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[DPY19L3]] | -0.39 | -0.29 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICU3]] | B | MICU3 activity raises PDGFC's level | lines that do not express MICU3 (19) vs lines expressing it (31) | 3.39× lower at baseline in the lines without MICU3 | 0.029 | ⚠ within organs, on part of the lines; co-absent genes; also absent: BVES-AS1, EVL, MIR130AHG |
| [[RAB32]] | B | RAB32 activity raises PDGFC's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 5.59× lower at baseline in the lines without RAB32 | 0.050 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[EML1]] | B | EML1 activity raises PDGFC's level | lines that do not express EML1 (13) vs lines expressing it (37) | 3.59× lower at baseline in the lines without EML1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PDGFC's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[GLRB]] | C | GLRB activity raises PDGFC's level | lines that do not express GLRB (19) vs lines expressing it (31) | 3.66× lower at baseline in the lines without GLRB | 0.025 | ⚠ within organs, on part of the lines; also absent: ELOVL4, LRP1B, PRR16; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPGR]] | B | PDGFC activity lowers RPGR's level | lines that do not express PDGFC (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without PDGFC | 0.058 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, GLRB, DNAH11 |
| [[DNAH11]] | C | PDGFC activity raises DNAH11's level | lines that do not express PDGFC (13) vs lines expressing it (37) | 3.92× lower at baseline in the lines without PDGFC | 0.042 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, GLRB, DNAH11; co-absent with the target |
| [[FAT4]] | C | PDGFC activity raises FAT4's level | lines that do not express PDGFC (13) vs lines expressing it (37) | 5.24× lower at baseline in the lines without PDGFC | 0.060 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, GLRB, DNAH11; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 24.3); signed map (41.2, 25.5). **Vector** length 98.6, 29.7% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | -8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +1.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.1 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.4 | -10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -13.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -10.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:156,760,454-156,971,799 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCDGF, fallotein |
| Gene groups (HGNC) | PDGF family ligands |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 2 pathways, smallest: Signaling by PDGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRA1](https://www.uniprot.org/uniprotkb/Q9NRA1) (Platelet-derived growth factor C):

> Growth factor that plays an essential role in the regulation of embryonic development, cell proliferation, cell migration, survival and chemotaxis. Potent mitogen and chemoattractant for cells of mesenchymal origin. Required for normal skeleton formation during embryonic development, especially for normal development of the craniofacial skeleton and for normal development of the palate. Required for normal skin morphogenesis during embryonic development. Plays an important role in wound …

**Summary**, from NCBI Gene [56034](https://www.ncbi.nlm.nih.gov/gene/56034):

> The protein encoded by this gene is a member of the platelet-derived growth factor family. The four members of this family are mitogenic factors for cells of mesenchymal origin and are characterized by a core motif of eight cysteines. This gene product appears to form only homodimers. It differs from the platelet-derived growth factor alpha and beta polypeptides in having an unusual N-terminal domain, the CUB domain. Alternatively spliced transcript variants have been found for this gene. …

**Accessions** — [HGNC:8801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8801) · Entrez [56034](https://www.ncbi.nlm.nih.gov/gene/56034) · UniProt [Q9NRA1](https://www.uniprot.org/uniprotkb/Q9NRA1) · Ensembl [ENSG00000145431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145431)

## Data

Gene col 6993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6993); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6993]; `tensor/DDL_lfc|DDL_z.npy` [6993]; `embed/gene_vectors.npy` [6993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6993 or target_col == 6993). Every well: [[PDGFC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
