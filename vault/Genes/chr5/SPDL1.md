---
symbol: "SPDL1"
type: "gene"
col: 466
ensembl_id: "ENSG00000040275"
name: "spindle apparatus coiled-coil protein 1"
location: "5q35.1"
module: 22
arm: "+"
pooled_cpm: 41.62
n_lines_expressing: 47
n_dd_up: 39
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 42
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SPDL1

*spindle apparatus coiled-coil protein 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.09× (z +16.2, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +11.8, q 3e-30, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.599× (z -6.1, q 5e-07, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.630× (z -5.5, q 6e-06, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMMR]] (+0.84, fdr 7e-06), [[ASPM]] (+0.79, fdr 7e-06), [[CIP2A]] (+0.77, fdr 7e-06); moves opposite to [[RPS25]] (-0.61, fdr 3e-05), [[RPS5]] (-0.60, fdr 1e-05), [[RPLP2]] (-0.60, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); 42 go from it, the strongest it → [[DEPDC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.09×** | +16.2 | 0e+00 | 35/36 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **3.58×** | +15.2 | 0e+00 | 41/43 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.87×** | +12.1 | 2e-31 | 43/45 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +11.8 | 3e-30 | 39/45 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.87×** | +10.5 | 9e-24 | 37/45 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.11×** | +8.2 | 2e-14 | 33/39 (NCI-H2347, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.94×** | +7.9 | 3e-13 | 39/45 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.83×** | +7.2 | 5e-11 | 32/45 (HS-578T, SW 900, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.76×** | +6.7 | 1e-09 | 39/45 (HT-29, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.43×** | +6.0 | 1e-07 | 37/45 (SW 900, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.0 | 1e-07 | 29/45 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.61×** | +5.2 | 8e-06 | 31/44 (SW 900, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.51×** | +4.9 | 4e-05 | 29/44 (SW 900, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.49×** | +4.5 | 2e-04 | 27/45 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.4 | 4e-04 | 27/45 (SW1417, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 8e-04 | 21/45 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.001 | 22/45 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.004 | 22/45 (PANC-1, A-172, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.007 | 23/45 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.009 | 21/45 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.011 | 18/45 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.022 | 19/45 (SW 900, NCI-H23, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.029 | 17/45 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.038 | 20/45 (SW 900, A549, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.039 | 12/45 (PANC-1, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.040 | 18/45 (NCI-H23, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 466.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -6.1 | 5e-07 | 30/45 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.715×** | -5.7 | 4e-06 | 39/45 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -5.5 | 6e-06 | 28/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -5.4 | 1e-05 | 25/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -4.8 | 2e-04 | 26/45 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.706×** | -4.0 | 0.005 | 24/45 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.736×** | -3.7 | 0.019 | 25/45 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.740×** | -3.6 | 0.022 | 20/45 (RKO, A-172, …) | inconsistent across doses | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.665×** | -3.5 | 0.031 | 21/45 (A-427, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **0.578×** | -3.4 | 0.034 | 17/38 (A-172, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.698×** | -3.3 | 0.042 | 20/45 (A-172, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.049 | 15/45 (NCI-H2030, CHP-212, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 55.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.0) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 29.1 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +15.1) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[SW 900 (line)]] | alt | 67.5 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 46.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.4) | — |
| [[J82 (line)]] | alt | 71.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.85× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Digitoxin (drug)]] 5 µM 0.271× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 24.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 71.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Digitoxin (drug)]] 5 µM 0.327× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.352× (z -8.5) |
| [[SW480 (line)]] | alt | 34.0 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -10.9) |
| [[A498 (line)]] | wt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 41.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.7) | — |
| [[H4 (line)]] | wt | 32.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.84× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Selinexor (drug)]] 5 µM 0.226× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.122× (z -8.6) |
| [[LoVo (line)]] | wt | 26.2 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.61× (z +9.3) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.7× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 40.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.62× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 28.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.0) | — |
| [[A-172 (line)]] | wt | 233 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 26.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[KATO III (line)]] | alt | 23.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SHP-77 (line)]] | alt | 39.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.5) |
| [[A-427 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.84× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H23 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.7) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[RKO (line)]] | wt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.2) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMMR]] | +0.84 | +0.87 / +0.81 | both halves | 7e-06 | STRING 555 |
| [[ASPM]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 | STRING 459 |
| [[CIP2A]] | +0.77 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[DEPDC1]] | +0.77 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[KIF11]] | +0.76 | +0.68 / +0.83 | both halves | 7e-06 | STRING 679 |
| [[MKI67]] | +0.74 | +0.63 / +0.86 | both halves | 7e-06 |  |
| [[KNSTRN]] | +0.73 | +0.66 / +0.78 | both halves | 7e-06 | STRING 466 |
| [[SMC4]] | +0.73 | +0.72 / +0.80 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 526 |
| [[PRC1]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 410 |
| [[GEN1]] | +0.73 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.72 | +0.63 / +0.80 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 520 |
| [[SGO1]] | +0.72 | +0.70 / +0.79 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 456 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS25]] | -0.61 | -0.72 / -0.44 | both halves | 3e-05 |  |
| [[RPS5]] | -0.60 | -0.67 / -0.49 | both halves | 1e-05 | STRING 464 |
| [[RPLP2]] | -0.60 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[RPL27A]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[RPS21]] | -0.59 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[RPL31]] | -0.59 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[RPS19]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[SNHG25]] | -0.59 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[RPL32]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PLD3]] | -0.58 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[RPS14]] | -0.58 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[RPL36A]] | -0.58 | -0.63 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises SPDL1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.27× lower at baseline in the lines without MYBL1 | 0.066 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SPDL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDC20]] | C | CDC20 activity raises SPDL1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.01× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises SPDL1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without NDC80 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 0, C 42. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DEPDC1]] | C | [[CDCA3]], SPDL1 activity raises DEPDC1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CENPF]] | C | [[CDCA3]], SPDL1 activity raises CENPF's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.80× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[DLGAP5]] | C | [[CDCA3]], SPDL1 activity raises DLGAP5's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.68× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[NDC80]] | C | [[CDCA3]], SPDL1 activity raises NDC80's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.45× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[BUB1B]] | C | [[CDCA3]], SPDL1 activity raises BUB1B's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.34× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[GTSE1]] | C | [[CDCA3]], SPDL1 activity raises GTSE1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.33× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[BIRC5]] | C | [[CDCA3]], SPDL1 activity raises BIRC5's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.27× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[KIF15]] | C | [[CDCA3]], SPDL1 activity raises KIF15's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.25× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[KIF23]] | C | [[CDCA3]], SPDL1 activity raises KIF23's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.24× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CENPE]] | C | [[CDCA3]], SPDL1 activity raises CENPE's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.06× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[KIF2C]] | C | [[CDCA3]], SPDL1 activity raises KIF2C's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; co-absent genes |
| [[CDKN3]] | C | [[CDCA3]], SPDL1 activity raises CDKN3's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.3, -56.4); signed map (-50.3, -45.1). **Vector** length 114, 37.4% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.56 to 60); *DREAM G2/M down* (control, mean cos +0.63 to 28); *E2F targets* (hallmark, mean cos +0.55 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +8.3 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +7.7 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.5 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.4 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +2.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | -3.9 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | spindle apparatus coiled-coil protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:169,583,636-169,604,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20364, hSpindly; previously CCDC99 |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EA4](https://www.uniprot.org/uniprotkb/Q96EA4) (Protein Spindly):

> Required for the localization of dynein and dynactin to the mitotic kinetochore. Dynein is believed to control the initial lateral interaction between the kinetochore and spindle microtubules and to facilitate the subsequent formation of end-on kinetochore-microtubule attachments mediated by the NDC80 complex. Also required for correct spindle orientation. Does not appear to be required for the removal of spindle assembly checkpoint (SAC) proteins from the kinetochore upon bipolar spindle …

**Summary**, from NCBI Gene [54908](https://www.ncbi.nlm.nih.gov/gene/54908):

> This gene encodes a coiled-coil domain-containing protein that functions in mitotic spindle formation and chromosome segregation. The encoded protein plays a role in coordinating microtubule attachment by promoting recruitment of dynein proteins, and in mitotic checkpoint signaling. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:26010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26010) · Entrez [54908](https://www.ncbi.nlm.nih.gov/gene/54908) · UniProt [Q96EA4](https://www.uniprot.org/uniprotkb/Q96EA4) · Ensembl [ENSG00000040275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040275)

## Data

Gene col 466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 466); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 466]; `tensor/DDL_lfc|DDL_z.npy` [466]; `embed/gene_vectors.npy` [466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 466 or target_col == 466). Every well: [[SPDL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPDL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
