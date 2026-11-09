---
symbol: "ZNF33A"
type: "gene"
col: 12100
ensembl_id: "ENSG00000189180"
name: "zinc finger protein 33A"
location: "10p11.1"
module: 110
arm: "+"
pooled_cpm: 98.28
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 45
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ZNF33A

*zinc finger protein 33A* — 10p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.21× (z +5.4, q 3e-05, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.295× (z -35.4, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.302× (z -34.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL54]] (+0.55, fdr 3e-05), [[NABP2]] (+0.53, fdr 7e-05), [[ZC3H7A]] (+0.53, fdr 3e-05); moves opposite to [[PNP]] (-0.52, fdr 3e-05), [[MICAL1]] (-0.51, fdr 4e-05), [[NBPF9]] (-0.51, fdr 4e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIK3CB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +5.4 | 3e-05 | 22/47 (SW48, HepG2/C3A, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.16× | +4.3 | 0.005 | 6/49 (J82, NCI-H2030, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.005 | 20/50 (SW480, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.17× | +4.0 | 0.008 | 15/50 (SW48, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.14× | +3.8 | 0.018 | 11/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.055 | 17/49 (BT-474, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 24 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.295×** | -35.4 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.302×** | -34.7 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.310×** | -34.0 | 0e+00 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.559×** | -23.8 | 0e+00 | 44/49 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.470×** | -21.9 | 0e+00 | 45/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -19.2 | 0e+00 | 39/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.520×** | -19.0 | 0e+00 | 47/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.530×** | -18.4 | 0e+00 | 42/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -16.2 | 0e+00 | 47/48 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -15.5 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -14.0 | 5e-43 | 44/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.621×** | -13.8 | 1e-41 | 42/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.622×** | -13.7 | 2e-41 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -12.8 | 4e-36 | 36/48 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -12.5 | 2e-34 | 44/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -11.8 | 2e-30 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -9.9 | 1e-21 | 32/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -9.3 | 3e-19 | 30/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -8.8 | 3e-17 | 24/48 (Panc 03.27, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.562×** | -8.7 | 7e-17 | 39/49 (NCI-H1792, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 89.9 | 0 | 17 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -20.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -24.1) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.264× (z -17.2) |
| [[SW480 (line)]] | alt | 108 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -29.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -29.2) |
| [[C-33 A (line)]] | alt | 221 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 69.9 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -20.2) |
| [[AsPC-1 (line)]] | alt | 97.6 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.170× (z -20.1) |
| [[C32 (line)]] | wt | 61.2 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -20.6) |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -15.5) |
| [[J82 (line)]] | alt | 102 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -28.8) ⚠ toxic; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.260× (z -17.6) |
| [[A-172 (line)]] | wt | 84.5 | 1 (1 ⚠) | 8 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.93× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.300× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -12.6) |
| [[HOP62 (line)]] | alt | 71.2 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.255× (z -17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -15.3) |
| [[LoVo (line)]] | wt | 119 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -21.2) |
| [[RKO (line)]] | wt | 70.6 | 0 | 9 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.167× (z -18.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.261× (z -14.0) |
| [[SW1417 (line)]] | alt | 106 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -14.1) |
| [[A549 (line)]] | wt | 98.5 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -19.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -18.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -16.9) |
| [[PANC-1 (line)]] | alt | 83.6 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 97.8 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -17.7) |
| [[COLO 205 (line)]] | alt | 81.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -17.3) |
| [[H4 (line)]] | wt | 70.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0902× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -12.3) |
| [[HS-578T (line)]] | alt | 52.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -15.8) |
| [[HT-29 (line)]] | alt | 129 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.303× (z -15.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.5) |
| [[LS 180 (line)]] | wt | 143 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -20.3) |
| [[NCI-H1573 (line)]] | alt | 89.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -12.1) |
| [[SHP-77 (line)]] | alt | 95.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.8) |
| [[SW 900 (line)]] | alt | 76.6 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.312× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.313× (z -12.9) |
| [[Hs 766T (line)]] | wt | 76.5 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.294× (z -13.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 83.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -16.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.331× (z -14.4) |
| [[A498 (line)]] | wt | 79.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -17.2) |
| [[BT-474 (line)]] | alt | 106 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 87.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -17.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.259× (z -16.3) |
| [[A-427 (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.368× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -13.0) |
| [[HCT15 (line)]] | alt | 194 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.219× (z -17.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -15.3) |
| [[KATO III (line)]] | alt | 86.6 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.277× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -13.8) |
| [[SNU-1 (line)]] | wt | 95.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -12.9) |
| [[SW48 (line)]] | wt | 128 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -15.9) |
| [[AN3 CA (line)]] | alt | 73.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -10.6) |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.129× (z -8.8) |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 1 | — | [[Niclosamide (olamine) (drug)]] 0.05 µM 0.0732× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL54]] | +0.55 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[NABP2]] | +0.53 | +0.44 / +0.37 | both halves | 7e-05 |  |
| [[ZC3H7A]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ANAPC16]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ZNF33B]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 | same gene group |
| [[ZNF428]] | +0.52 | +0.43 / +0.32 | both halves | 2e-04 | same gene group |
| [[PPIL4]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TRIM23]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB5]] | +0.50 | +0.51 / +0.52 | both halves | 1e-05 | same gene group |
| [[FMC1]] | +0.50 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[ARFGEF2]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CILK1]] | +0.49 | +0.28 / +0.49 | both halves | 3e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNP]] | -0.52 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MICAL1]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[NBPF9]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[GALNT14]] | -0.49 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[CAP1]] | -0.49 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[TMEM171]] | -0.48 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CD59]] | -0.48 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[S100A11]] | -0.47 | -0.51 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CORO2B]] | -0.46 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[ABTB3]] | -0.46 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[UGGT2]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ADAM23]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[NBPF20]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CB]] | B | PIK3CB activity lowers ZNF33A's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[GALNT14]] | B | GALNT14 activity raises ZNF33A's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.20× lower at baseline in the lines without GALNT14 | 0.079 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TOP2A]] | B | TOP2A activity raises ZNF33A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIK3CA]] | B | PIK3CA activity lowers ZNF33A's level | compounds that target PIK3CA: 2 of 4 raise it (Bimiralisib, GSK1059615) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction -0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.4, -52.0); signed map (-12.1, 1.5). **Vector** length 77.3, 21.6% of its response variance represented; |z| ≥ 3 in 1,711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | -19.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | -12.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.8 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -7.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.9 | -16.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -15.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -9.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 33A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.1 — chr10:38,010,650-38,065,088 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX5, KOX31, KIAA0065, FLJ23404, ZZAPK; previously ZNF33, ZNF11A |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by KRAB-ZFP proteins; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06730](https://www.uniprot.org/uniprotkb/Q06730) (Zinc finger protein 33A):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7581](https://www.ncbi.nlm.nih.gov/gene/7581):

> Predicted to enable transcription cis-regulatory region binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13096) · Entrez [7581](https://www.ncbi.nlm.nih.gov/gene/7581) · UniProt [Q06730](https://www.uniprot.org/uniprotkb/Q06730) · Ensembl [ENSG00000189180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189180)

## Data

Gene col 12100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12100); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12100]; `tensor/DDL_lfc|DDL_z.npy` [12100]; `embed/gene_vectors.npy` [12100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12100 or target_col == 12100). Every well: [[ZNF33A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF33A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
