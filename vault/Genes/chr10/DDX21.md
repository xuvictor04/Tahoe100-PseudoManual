---
symbol: "DDX21"
type: "gene"
col: 9178
ensembl_id: "ENSG00000165732"
name: "DExD-box helicase 21"
location: "10q22.1"
module: 5
arm: "+"
pooled_cpm: 268.39
n_lines_expressing: 50
n_dd_up: 53
n_dd_down: 6
n_dd_up_clean: 28
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DDX21

*DExD-box helicase 21* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 53 drug-doses (25 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +14.6, q 1e-45, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.66× (z +11.3, q 1e-27, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.740× (z -5.0, q 3e-04, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~90% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.681× (z -4.3, q 0.004, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS1]] (+0.78, fdr 7e-06), [[GTPBP4]] (+0.77, fdr 7e-06), [[PNO1]] (+0.76, fdr 7e-06); moves opposite to [[TMEM59]] (-0.66, fdr 7e-06), [[MPC2]] (-0.65, fdr 7e-06), [[ATP5IF1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 25 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 53 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.53×** | +14.6 | 1e-45 | 49/49 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.33×** | +13.4 | 1e-38 | 44/44 (LoVo, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.98×** | +11.7 | 2e-29 | 45/45 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +11.3 | 1e-27 | 43/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.20×** | +9.1 | 1e-17 | 48/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +9.1 | 1e-17 | 45/48 (AN3 CA, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +8.6 | 9e-16 | 47/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **2.13×** | +8.4 | 2e-15 | 45/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.64×** | +8.0 | 6e-14 | 35/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.94×** | +7.4 | 8e-12 | 43/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.88×** | +7.3 | 1e-11 | 40/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.84×** | +7.1 | 8e-11 | 40/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +6.9 | 2e-10 | 42/48 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +6.4 | 8e-09 | 44/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.82×** | +6.3 | 1e-08 | 40/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.70×** | +6.0 | 6e-08 | 47/48 (SW1417, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.59×** | +5.8 | 3e-07 | 47/48 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +5.7 | 4e-07 | 40/48 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +5.5 | 1e-06 | 35/49 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 6e-06 | 42/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.33×** | +5.1 | 7e-06 | 47/48 (CFPAC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.6 | 7e-05 | 34/48 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.52×** | +4.6 | 8e-05 | 39/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.11×** | +4.5 | 1e-04 | 45/48 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.2 | 6e-04 | 39/48 (NCI-H1792, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.740×** | -5.0 | 3e-04 | 31/48 (RKO, LoVo, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.681×** | -4.3 | 0.004 | 36/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.725×** | -3.8 | 0.031 | 37/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.737×** | -3.6 | 0.050 | 31/48 (LoVo, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.573×** | -3.4 | 0.078 | 34/50 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.816×** | -3.3 | 0.087 | 27/48 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 160 | 14 (11 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.84× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 189 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +16.3) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.68× (z +16.0) | — |
| [[H4 (line)]] | wt | 187 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.65× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 157 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.65× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 191 | 9 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 254 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 139 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.36× (z +15.7) | — |
| [[Hs 766T (line)]] | wt | 241 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.83× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 326 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.75× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 220 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 229 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.18× (z +12.0) | — |
| [[SW480 (line)]] | alt | 309 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.40× (z +13.6) | — |
| [[A549 (line)]] | wt | 286 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +10.3) | — |
| [[C32 (line)]] | wt | 148 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 359 | 6 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.28× (z +10.4) | [[Adagrasib (drug)]] 0.05 µM 0.631× (z -13.9) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 140 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.43× (z +10.0) | — |
| [[A498 (line)]] | wt | 392 | 6 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.88× (z +11.0) | — |
| [[LoVo (line)]] | wt | 308 | 4 (4 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Selinexor (drug)]] 5 µM 0.460× (z -11.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LOX-IMVI (line)]] | wt | 271 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 176 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 379 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 228 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.41× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 178 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 153 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 184 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +10.2) | — |
| [[J82 (line)]] | alt | 258 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 168 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LS 180 (line)]] | wt | 220 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Selinexor (drug)]] 5 µM 0.416× (z -11.4) ⚠ cell-cycle shift, explains ~90% of this change |
| [[PANC-1 (line)]] | alt | 513 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +10.5) | — |
| [[RKO (line)]] | wt | 502 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Selinexor (drug)]] 5 µM 0.469× (z -12.3) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SW1417 (line)]] | alt | 274 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[C-33 A (line)]] | alt | 247 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.68× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 124 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 269 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 307 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.67× (z +10.0) | — |
| [[A-427 (line)]] | wt | 298 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.97× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 264 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.58× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.497× (z -9.8) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HCT15 (line)]] | alt | 225 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.70× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 339 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 175 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 329 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 455 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.89× (z +16.4) | — |
| [[CHP-212 (line)]] | wt | 292 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SHP-77 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0773× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 665 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | +0.78 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 | STRING 813 |
| [[PNO1]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 618 |
| [[WDR4]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 544 |
| [[NOP16]] | +0.74 | +0.84 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NOLC1]] | +0.73 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 657 |
| [[PINX1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[PUM3]] | +0.71 | +0.75 / +0.67 | both halves | 7e-06 | STRING 636 |
| [[LETM1]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[DDX31]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 | same gene group; STRING 594 |
| [[NOP2]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 | pathway: rRNA processing; STRING 761 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | -0.66 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[MPC2]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ATP5IF1]] | -0.63 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[MBIP]] | -0.63 | -0.53 / -0.64 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[CENPC]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[CCNG2]] | -0.61 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[DCTN3]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.59 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[NPC2]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.58 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[OGA]] | -0.58 | -0.46 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity lowers DDX21's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.50× higher at baseline in the lines without ADD3 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.5, -36.4); signed map (-2.1, -47.5). **Vector** length 94.5, 52.1% of its response variance represented; |z| ≥ 3 in 2,070 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.63 to 13); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.57 to 11); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.2 | +9.1 |
|  | [[EX229 (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.8 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +6.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -7.5 | -5.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.4 | +7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -4.1 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | DExD-box helicase 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:68,956,135-68,985,068 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RH-II/GU, GURDB, Gu-alpha |
| Gene groups (HGNC) | DEAD-box helicases; B-WICH chromatin-remodelling complex subunits |
| Hallmark sets | UV_RESPONSE_UP, MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: B-WICH complex positively regulates rRNA expression; Positive epigenetic regulation of rRNA expression; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR30](https://www.uniprot.org/uniprotkb/Q9NR30) (Nucleolar RNA helicase 2):

> RNA helicase that acts as a sensor of the transcriptional status of both RNA polymerase (Pol) I and II: promotes ribosomal RNA (rRNA) processing and transcription from polymerase II (Pol II). Binds various RNAs, such as rRNAs, snoRNAs, 7SK and, at lower extent, mRNAs. In the nucleolus, localizes to rDNA locus, where it directly binds rRNAs and snoRNAs, and promotes rRNA transcription, processing and modification. Required for rRNA 2'-O-methylation, possibly by promoting the recruitment of …

**Summary**, from NCBI Gene [9188](https://www.ncbi.nlm.nih.gov/gene/9188):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2744) · Entrez [9188](https://www.ncbi.nlm.nih.gov/gene/9188) · UniProt [Q9NR30](https://www.uniprot.org/uniprotkb/Q9NR30) · Ensembl [ENSG00000165732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165732)

## Data

Gene col 9178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9178); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9178]; `tensor/DDL_lfc|DDL_z.npy` [9178]; `embed/gene_vectors.npy` [9178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9178 or target_col == 9178). Every well: [[DDX21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
