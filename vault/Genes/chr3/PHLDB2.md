---
symbol: "PHLDB2"
type: "gene"
col: 6934
ensembl_id: "ENSG00000144824"
name: "pleckstrin homology like domain family B member 2"
location: "3q13.2"
module: 66
arm: "+"
pooled_cpm: 223.35
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 44
n_dd_up_clean: 17
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# PHLDB2

*pleckstrin homology like domain family B member 2* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.69× (z +8.2, q 2e-13, up in 27 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.356× (z -17.0, q 0e+00, down in 34 of 37 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.569× (z -13.1, q 5e-37, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROS1]] (+0.75, fdr 7e-06), [[TGFB2]] (+0.72, fdr 7e-06), [[LINC02015]] (+0.63, fdr 8e-06); moves opposite to [[ATPAF2]] (-0.46, fdr 2e-04), [[PGF]] (-0.45, fdr 2e-04), [[C2CD2]] (-0.43, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NTN4]] → it (grade B ⚠); 2 go from it, the strongest it → [[GPR141]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **1.69×** | +8.2 | 2e-13 | 27/39 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +7.0 | 9e-10 | 21/37 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **2.10×** | +6.4 | 3e-08 | 24/37 (A-172, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.1 | 1e-07 | 23/38 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 2e-07 | 22/37 (A-172, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +5.6 | 2e-06 | 20/37 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.87×** | +5.4 | 6e-06 | 22/39 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +5.4 | 6e-06 | 21/37 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 21/38 (A-172, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 19/36 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 18/38 (A-172, SW 900, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 19/37 (A-172, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.5 | 3e-04 | 18/38 (LoVo, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 5e-04 | 17/36 (A-172, HOP62, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +4.2 | 9e-04 | 17/36 (A-172, HS-578T, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.012 | 14/37 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[BI-3406 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.013 | 17/37 (A-172, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.356×** | -17.0 | 0e+00 | 34/37 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.361×** | -16.7 | 0e+00 | 34/37 (Hs 766T, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.429×** | -13.9 | 1e-41 | 32/37 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -13.1 | 5e-37 | 29/38 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.465×** | -12.1 | 2e-31 | 32/36 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -9.2 | 3e-18 | 29/37 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.580×** | -8.9 | 3e-17 | 30/37 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -8.1 | 3e-14 | 26/37 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -8.1 | 3e-14 | 26/37 (BT-474, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -8.0 | 9e-14 | 25/37 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -7.7 | 9e-13 | 21/37 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.629×** | -7.6 | 1e-12 | 25/37 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.657×** | -6.9 | 3e-10 | 29/37 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.656×** | -6.6 | 1e-09 | 23/37 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.680×** | -6.3 | 1e-08 | 26/38 (Hs 766T, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.521×** | -5.6 | 8e-07 | 24/37 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.735×** | -5.1 | 1e-05 | 20/37 (BT-474, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.744×** | -4.6 | 1e-04 | 22/37 (Panc 03.27, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.823×** | -4.5 | 2e-04 | 17/37 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.595×** | -4.5 | 2e-04 | 21/37 (NCI-H1573, J82, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.602×** | -4.4 | 3e-04 | 18/37 (LoVo, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.761×** | -4.2 | 6e-04 | 21/37 (Panc 03.27, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.628×** | -4.0 | 0.001 | 19/37 (J82, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 225 | 17 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +22.9) | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 219 | 1 | 18 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.240× (z -17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.457× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 268 | 0 | 16 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -16.7) |
| [[Hs 766T (line)]] | wt | 815 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.0) |
| [[A549 (line)]] | wt | 895 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -18.0) |
| [[BT-474 (line)]] | alt | 285 | 1 | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.147× (z -15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.158× (z -14.4) |
| [[J82 (line)]] | alt | 816 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 214 | 4 | 5 (3 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.90× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.445× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 567 | 1 | 8 (3 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.74× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.211× (z -13.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.289× (z -11.1) |
| [[SW480 (line)]] | alt | 145 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 250 | 0 | 7 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.297× (z -12.2) |
| [[HOP62 (line)]] | alt | 61.7 | 6 | 0 | [[Trametinib (drug)]] 5 µM 4.33× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 507 | 3 (1 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.68× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -21.0) |
| [[NCI-H1573 (line)]] | alt | 351 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -24.5) |
| [[NCI-H1792 (line)]] | alt | 106 | 1 | 5 (3 ⚠) | [[Trametinib (drug)]] 5 µM 2.64× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.7) |
| [[A498 (line)]] | wt | 160 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 117 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.297× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 229 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -18.0) |
| [[LS 180 (line)]] | wt | 131 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.0) |
| [[SHP-77 (line)]] | alt | 78.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.2) |
| [[A-427 (line)]] | wt | 104 | 1 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.69× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 228 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -18.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 153 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 2.88× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.8) |
| [[SW 1271 (line)]] | alt | 648 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -10.8) |
| [[SW 900 (line)]] | alt | 94.4 | 3 | 1 (1 ⚠) | [[Trametinib (drug)]] 5 µM 3.43× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 295 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -20.4) |
| [[C32 (line)]] | wt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 304 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -14.5) |
| [[SW 1088 (line)]] | alt | 199 | 0 | 2 | — | [[Decitabine (drug)]] 0.5 µM 0.0841× (z -9.8) |
| [[HCT15 (line)]] | alt | 83.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -9.5) |
| [[HS-578T (line)]] | alt | 214 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.6) |
| [[SNU-423 (line)]] | alt | 415 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.1) |
| [[SW1417 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 97.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 55.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 20.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 34.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROS1]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[TGFB2]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LINC02015]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[SEMA3C]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[IL1R1]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CCBE1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[OLR1]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[TCIM]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DSEL]] | +0.55 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[RHCG]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RAB31]] | +0.55 | +0.40 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATPAF2]] | -0.46 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[PGF]] | -0.45 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[C2CD2]] | -0.43 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[COQ4]] | -0.43 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SHANK1]] | -0.41 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[SH2B3]] | -0.41 | -0.34 / -0.41 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | NTN4 activity strengthens PHLDB2's drug response | lines that do not express NTN4 (11) vs lines expressing it (28) | the lines without NTN4 respond 0.62× as strongly (z diff +2.50); strongest at Idarubicin (hydrochloride) 5 µM: 0.76x vs 0.45x (z diff +4.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers PHLDB2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KRT6A]] | B | KRT6A activity raises PHLDB2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 1.93× lower at baseline in the lines without KRT6A | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR141]] | B | PHLDB2 activity lowers GPR141's level | lines that do not express PHLDB2 (11) vs lines expressing it (39) | 1.22× higher at baseline in the lines without PHLDB2 | 0.086 | ⚠ within organs, on part of the lines; also absent: MDFIC, KITLG, CCDC85A |
| [[TPM4]] | B | PHLDB2 activity raises TPM4's level | lines that do not express PHLDB2 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without PHLDB2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MDFIC, KITLG, CCDC85A |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.0, 20.7); signed map (47.4, 20.9). **Vector** length 120, 36.5% of its response variance represented; |z| ≥ 3 in 1,875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.9 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +4.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -6.9 |
|  | [[Afatinib (drug)]] 5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology like domain family B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:111,732,497-111,976,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LL5beta, FLJ21791, LL5b |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SQ0](https://www.uniprot.org/uniprotkb/Q86SQ0) (Pleckstrin homology-like domain family B member 2):

> Seems to be involved in the assembly of the postsynaptic apparatus. May play a role in acetyl-choline receptor (AChR) aggregation in the postsynaptic membrane (By similarity).

**Summary**, from NCBI Gene [90102](https://www.ncbi.nlm.nih.gov/gene/90102):

> Enables cadherin binding activity. Involved in several processes, including basement membrane organization; negative regulation of cellular component organization; and negative regulation of wound healing, spreading of epidermal cells. Located in several cellular components, including basal cortex; focal adhesion; and podosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29573) · Entrez [90102](https://www.ncbi.nlm.nih.gov/gene/90102) · UniProt [Q86SQ0](https://www.uniprot.org/uniprotkb/Q86SQ0) · Ensembl [ENSG00000144824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144824)

## Data

Gene col 6934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6934); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6934]; `tensor/DDL_lfc|DDL_z.npy` [6934]; `embed/gene_vectors.npy` [6934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6934 or target_col == 6934). Every well: [[PHLDB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLDB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
