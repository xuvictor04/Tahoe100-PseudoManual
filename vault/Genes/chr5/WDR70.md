---
symbol: "WDR70"
type: "gene"
col: 1333
ensembl_id: "ENSG00000082068"
name: "WD repeat domain 70"
location: "5p13.2"
module: 230
arm: "+"
pooled_cpm: 161.8
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/230"]
generated_by: "tahoemap"
---

# WDR70

*WD repeat domain 70* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +16.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.447× (z -19.4, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX8]] (+0.70, fdr 1e-05), [[DIS3L2]] (+0.69, fdr 1e-05), [[WDR7]] (+0.67, fdr 7e-06); moves opposite to [[NIPBL-DT]] (-0.67, fdr 3e-05), [[LINC00938]] (-0.60, fdr 4e-05), [[UPK2]] (-0.56, fdr 2e-04).
> It is in [[Module 230]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +16.7 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +12.0 | 1e-30 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +10.6 | 6e-24 | 48/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.19× | +4.1 | 0.006 | 21/48 (NCI-H1573, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.44× | +3.3 | 0.12 | 28/49 (BT-474, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.44× | +3.2 | 0.12 | 29/50 (NCI-H23, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.21× | +3.1 | 0.15 | 22/48 (NCI-H23, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1333.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.447×** | -19.4 | 0e+00 | 48/49 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -11.9 | 6e-30 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.535×** | -10.6 | 4e-24 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.568×** | -9.3 | 3e-18 | 36/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.583×** | -9.2 | 5e-18 | 46/49 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.601×** | -8.0 | 1e-13 | 37/45 (RKO, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.642×** | -7.6 | 3e-12 | 39/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -7.3 | 2e-11 | 41/47 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.685×** | -6.4 | 7e-09 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -6.4 | 1e-08 | 37/50 (NCI-H23, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -6.1 | 4e-08 | 37/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.708×** | -5.7 | 7e-07 | 35/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -5.1 | 1e-05 | 30/49 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.761×** | -4.5 | 3e-04 | 29/48 (A498, C32, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.771×** | -4.4 | 4e-04 | 30/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.7 | 0.007 | 27/48 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.693×** | -3.3 | 0.037 | 26/48 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.052 | 21/49 (CHP-212, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 210 | 3 | 10 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 166 | 1 | 11 (10 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -20.8) |
| [[C32 (line)]] | wt | 172 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 147 | 3 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -20.2) |
| [[A549 (line)]] | wt | 128 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.70× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.9) |
| [[HOP62 (line)]] | alt | 153 | 1 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -17.8) |
| [[LoVo (line)]] | wt | 195 | 4 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -12.1) |
| [[PANC-1 (line)]] | alt | 150 | 1 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.218× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -17.4) |
| [[SHP-77 (line)]] | alt | 239 | 3 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.391× (z -13.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 156 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.337× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.7) |
| [[A-427 (line)]] | wt | 216 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 79.2 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -14.6) |
| [[LS 180 (line)]] | wt | 127 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.454× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 196 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 427 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 198 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -19.7) |
| [[SW 900 (line)]] | alt | 156 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -18.7) |
| [[SW1417 (line)]] | alt | 189 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -18.5) |
| [[HepG2_C3A (line)]] | wt | 124 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.5) |
| [[J82 (line)]] | alt | 211 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -18.5) |
| [[A498 (line)]] | wt | 129 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.4) |
| [[COLO 205 (line)]] | alt | 137 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 134 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.18× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -8.7) |
| [[Hs 766T (line)]] | wt | 157 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -17.1) |
| [[hTERT-HPNE (line)]] | wt | 142 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.2) |
| [[KATO III (line)]] | alt | 107 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 133 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.376× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 184 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.7) |
| [[SNU-423 (line)]] | alt | 152 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -18.7) |
| [[A-172 (line)]] | wt | 115 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.2) |
| [[BT-474 (line)]] | alt | 198 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.06× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.0) |
| [[H4 (line)]] | wt | 145 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.56× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.8) |
| [[HS-578T (line)]] | alt | 156 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.9) |
| [[SNU-1 (line)]] | wt | 169 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.6) |
| [[AN3 CA (line)]] | alt | 227 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.0) |
| [[C-33 A (line)]] | alt | 137 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 140 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.3) |
| [[HCT15 (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 94.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -16.2) |
| [[RKO (line)]] | wt | 149 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0957× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 137 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.64× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -16.0) |
| [[SW48 (line)]] | wt | 140 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.74× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.1) |
| [[NCI-H661 (line)]] | alt | 262 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX8]] | +0.70 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.69 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[WDR7]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | same gene group |
| [[PWP1]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[VPS50]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[VPS13B]] | +0.63 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CIAO1]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 | same gene group |
| [[SPIDR]] | +0.61 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[CSTPP1]] | +0.61 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RAD54L2]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[THADA]] | +0.60 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[RPUSD1]] | +0.60 | +0.37 / +0.50 | both halves | 8e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPBL-DT]] | -0.67 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[LINC00938]] | -0.60 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[UPK2]] | -0.56 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[SIX4]] | -0.56 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[GNAS]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[BCL2L2-PABPN1]] | -0.55 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[SATB2-AS1]] | -0.55 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[MKLN1-AS]] | -0.54 | -0.19 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[CSRP2]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[EPHX1]] | -0.54 | -0.20 / -0.36 | both halves | 7e-04 |  |
| [[BCL2L2]] | -0.53 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[NFKBID]] | -0.53 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[INTS6L]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers WDR70's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SIX4]] | B | SIX4 activity raises WDR70's level | lines that do not express SIX4 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without SIX4 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CPLANE1, FGFR1 |
| [[TBC1D19]] | C | TBC1D19 activity raises WDR70's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 230]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.8, -5.1); signed map (-18.7, -24.8). **Vector** length 104, 39.2% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +16.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +12.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | -1.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.2 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -16.6 | -19.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.5 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.2 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:37,379,285-37,753,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10233 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q9NW82](https://www.uniprot.org/uniprotkb/Q9NW82) carries no function annotation.

**Summary**, from NCBI Gene [55100](https://www.ncbi.nlm.nih.gov/gene/55100):

> Enables enzyme binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be located in nucleoplasm. Predicted to be active in nucleus and site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25495) · Entrez [55100](https://www.ncbi.nlm.nih.gov/gene/55100) · UniProt [Q9NW82](https://www.uniprot.org/uniprotkb/Q9NW82) · Ensembl [ENSG00000082068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082068)

## Data

Gene col 1333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1333); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1333]; `tensor/DDL_lfc|DDL_z.npy` [1333]; `embed/gene_vectors.npy` [1333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1333 or target_col == 1333). Every well: [[WDR70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
