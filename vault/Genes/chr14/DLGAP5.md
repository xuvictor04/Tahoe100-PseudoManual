---
symbol: "DLGAP5"
type: "gene"
col: 4766
ensembl_id: "ENSG00000126787"
name: "DLG associated protein 5"
location: "14q22.3"
module: 22
arm: "+"
pooled_cpm: 59.62
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 32
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DLGAP5

*DLG associated protein 5* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +10.8, q 2e-24, up in 30 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.23× (z +3.6, q 0.012, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.503× (z -11.9, q 1e-29, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~93% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.671× (z -6.8, q 9e-10, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOP2A]] (+0.96, fdr 7e-06), [[BUB1]] (+0.95, fdr 7e-06), [[TPX2]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.86×** | +10.8 | 2e-24 | 30/46 (NCI-H2030, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.84×** | +7.5 | 2e-11 | 34/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.78×** | +7.1 | 2e-10 | 30/45 (A-172, PANC-1, …) | two highest doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.49×** | +6.9 | 7e-10 | 39/46 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.71×** | +6.6 | 5e-09 | 29/45 (KATO III, NCI-H23, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **2.72×** | +6.4 | 1e-08 | 38/45 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.70×** | +6.3 | 2e-08 | 33/46 (PANC-1, NCI-H2347, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.67×** | +6.3 | 2e-08 | 32/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.66×** | +6.3 | 2e-08 | 36/45 (HT-29, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.59×** | +5.7 | 8e-07 | 30/45 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.55×** | +5.4 | 4e-06 | 30/46 (KATO III, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.51×** | +5.1 | 2e-05 | 31/46 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.46×** | +4.5 | 3e-04 | 24/40 (A-172, Panc 03.27, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.012 | 21/46 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.5 | 0.020 | 18/46 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.033 | 21/46 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.048 | 18/46 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.054 | 13/46 (RKO, SW 900, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.0 | 0.063 | 16/46 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.063 | 18/46 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.070 | 14/46 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.091 | 17/46 (NCI-H460, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.503×** | -11.9 | 1e-29 | 40/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.485×** | -8.7 | 6e-16 | 40/46 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.491×** | -8.2 | 5e-14 | 33/46 (SW48, H4, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.529×** | -7.5 | 1e-11 | 43/46 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.671×** | -6.8 | 9e-10 | 34/46 (LS 180, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.577×** | -6.7 | 2e-09 | 34/46 (C32, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **0.353×** | -6.6 | 2e-09 | 32/42 (A-427, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.599×** | -6.2 | 5e-08 | 29/46 (LOX-IMVI, SW48, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.614×** | -5.9 | 2e-07 | 38/46 (H4, SNU-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.717×** | -5.7 | 7e-07 | 29/46 (H4, NCI-H2030, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.638×** | -5.5 | 2e-06 | 39/46 (NCI-H2030, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.651×** | -5.2 | 8e-06 | 28/46 (BT-474, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.651×** | -5.2 | 8e-06 | 35/46 (A549, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.757×** | -4.8 | 7e-05 | 30/46 (A-427, HCT15, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.669×** | -4.7 | 1e-04 | 29/46 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.690×** | -4.2 | 0.001 | 24/46 (H4, HOP62, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.546×** | -3.9 | 0.003 | 26/46 (SHP-77, C32, …) | top dose only | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.813×** | -3.3 | 0.021 | 22/46 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.772×** | -2.9 | 0.087 | 17/45 (LS 180, A-427, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.844× | -2.9 | 0.091 | 17/46 (Hs 766T, CHP-212, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -2.9 | 0.091 | 18/46 (BT-474, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.721×** | -2.8 | 0.091 | 17/46 (SW 1271, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.777×** | -2.8 | 0.091 | 13/46 (NCI-H1573, SW48, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.847× | -2.8 | 0.091 | 17/46 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.643×** | -2.8 | 0.092 | 17/46 (NCI-H1573, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.795×** | -2.8 | 0.092 | 8/46 (C-33 A, NCI-H23, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +1.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 78.3 | 0 | 9 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.102× (z -16.7) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.226× (z -10.8) |
| [[SW48 (line)]] | wt | 84.3 | 0 | 7 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0885× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.189× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 48.9 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.105× (z -19.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.180× (z -10.4) |
| [[A-172 (line)]] | wt | 28.1 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.27× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.216× (z -13.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A-427 (line)]] | wt | 120 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.173× (z -19.9) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.322× (z -12.9) |
| [[A549 (line)]] | wt | 56.2 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.226× (z -10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.369× (z -10.3) |
| [[LS 180 (line)]] | wt | 44.2 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.122× (z -16.6) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.244× (z -11.2) |
| [[A498 (line)]] | wt | 38.3 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0835× (z -27.7) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.422× (z -9.6) |
| [[SNU-1 (line)]] | wt | 55.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.124× (z -9.5) |
| [[C32 (line)]] | wt | 46.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.164× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 34.1 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.12× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 139 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +16.2) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.199× (z -11.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H23 (line)]] | alt | 157 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.458× (z -8.6) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H2347 (line)]] | alt | 98.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.475× (z -8.7) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H460 (line)]] | wt | 49.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.399× (z -9.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[PANC-1 (line)]] | alt | 57.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 61.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.424× (z -8.7) ⚠ cell-cycle shift, explains ~93% of this change |
| [[BT-474 (line)]] | alt | 38.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.131× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.375× (z -9.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[HCT15 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.327× (z -9.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[HOP62 (line)]] | alt | 76.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.381× (z -9.9) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.236× (z -9.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[Panc 03.27 (line)]] | alt | 62.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 47.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.136× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 45.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP2A]] | +0.96 | +0.96 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 978 |
| [[BUB1]] | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 986 |
| [[TPX2]] | +0.94 | +0.93 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 978 |
| [[KIF4A]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 962 |
| [[CENPF]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 976 |
| [[KIF18A]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | STRING 945 |
| [[CENPE]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 957 |
| [[NEK2]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 963 |
| [[ARHGAP11A]] | +0.93 | +0.92 / +0.91 | both halves | 7e-06 | STRING 801 |
| [[BIRC5]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 967 |
| [[NDC80]] | +0.93 | +0.93 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 957 |
| [[CKAP2]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | STRING 838 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises DLGAP5's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without PIMREG | 0.010 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises DLGAP5's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without NEURL1B | 0.071 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PBK]] | C | PBK activity raises DLGAP5's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.06× lower at baseline in the lines without PBK | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises DLGAP5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without AURKB | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises DLGAP5's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.68× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises DLGAP5's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises DLGAP5's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises DLGAP5's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without NDC80 | 0.096 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[TP53]] | C | TP53 activity strengthens DLGAP5's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 16 not recorded | the TP53-altered lines respond 0.77× as strongly (z diff +0.75); strongest at Amsacrine 5 µM: 0.75x vs 0.43x (z diff +3.5) | 0.907 over the table, 0.092 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.965). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -56.4); signed map (-50.2, -42.9). **Vector** length 168, 65.9% of its response variance represented; |z| ≥ 3 in 1,573 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.77 to 60); *Mitotic Prometaphase* (reactome, mean cos +0.74 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.76 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +7.4 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.8 | +10.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.8 | +5.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.7 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.5 | +6.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +0.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.0 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -8.8 | -11.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -8.7 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -8.6 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.9 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -5.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.7 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.6 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | DLG associated protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,148,112-55,191,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0008, DLG1, HURP; previously DLG7 |
| Hallmark sets | MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 3 pathways, smallest: NOTCH3 Intracellular Domain Regulates Transcription; Signaling by NOTCH3; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15398](https://www.uniprot.org/uniprotkb/Q15398) (DLG-associated protein 5):

> Potential cell cycle regulator that may play a role in carcinogenesis of cancer cells. Mitotic phosphoprotein regulated by the ubiquitin-proteasome pathway. Key regulator of adherens junction integrity and differentiation that may be involved in CDH1-mediated adhesion and signaling in epithelial cells.

**Summary**, from NCBI Gene [9787](https://www.ncbi.nlm.nih.gov/gene/9787):

> Predicted to enable microtubule binding activity. Predicted to be involved in several processes, including centrosome localization; kinetochore assembly; and mitotic spindle organization. Located in cytosol; nucleus; and spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16864) · Entrez [9787](https://www.ncbi.nlm.nih.gov/gene/9787) · UniProt [Q15398](https://www.uniprot.org/uniprotkb/Q15398) · Ensembl [ENSG00000126787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126787)

## Data

Gene col 4766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4766); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4766]; `tensor/DDL_lfc|DDL_z.npy` [4766]; `embed/gene_vectors.npy` [4766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4766 or target_col == 4766). Every well: [[DLGAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
