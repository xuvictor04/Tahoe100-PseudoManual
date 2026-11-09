---
symbol: "RRM2"
type: "gene"
col: 10173
ensembl_id: "ENSG00000171848"
name: "ribonucleotide reductase regulatory subunit M2"
location: "2p25.1"
module: 6
arm: "+"
pooled_cpm: 147.02
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 57
n_dd_up_clean: 8
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 10
direction_downstream: 10
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RRM2

*ribonucleotide reductase regulatory subunit M2* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.93× (z +12.9, q 2e-35, up in 43 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.63× (z +5.9, q 3e-07, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (15 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.472× (z -12.3, q 9e-32, down in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.367× (z -12.0, q 8e-31, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG2]] (+0.89, fdr 7e-06), [[CENPK]] (+0.88, fdr 7e-06), [[FANCA]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TLCD3B]] → it (grade B ⚠); 10 go from it, the strongest it → cells under [[Auranofin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.93×** | +12.9 | 2e-35 | 43/46 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.44×** | +10.3 | 1e-22 | 36/41 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.01×** | +8.4 | 8e-15 | 27/45 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.04×** | +8.0 | 2e-13 | 33/42 (SNU-423, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.83×** | +7.3 | 3e-11 | 31/45 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.70×** | +6.4 | 1e-08 | 28/45 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.9 | 3e-07 | 24/45 (SW480, HT-29, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.39×** | +5.5 | 3e-06 | 35/46 (SW480, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.5 | 3e-06 | 14/47 (RKO, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.4 | 6e-04 | 27/45 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.1 | 0.002 | 32/45 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.0 | 0.002 | 20/45 (SW48, SW480, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.0 | 0.003 | 24/45 (SW480, SW48, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.015 | 20/45 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.016 | 26/46 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.018 | 23/45 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.031 | 18/45 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.031 | 24/45 (SW480, LS 180, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.041 | 16/45 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.041 | 13/45 (LoVo, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.472×** | -12.3 | 9e-32 | 40/45 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -12.0 | 8e-31 | 35/45 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.496×** | -11.3 | 2e-27 | 34/45 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.402×** | -10.9 | 1e-25 | 43/45 (LOX-IMVI, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.451×** | -8.0 | 2e-13 | 37/45 (KATO III, A-427, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.608×** | -7.2 | 6e-11 | 37/45 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.547×** | -7.0 | 3e-10 | 37/44 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.658×** | -6.9 | 3e-10 | 36/45 (HCT15, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.482×** | -6.9 | 3e-10 | 37/47 (A-427, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.489×** | -6.1 | 5e-08 | 34/45 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.688×** | -6.1 | 6e-08 | 35/45 (SHP-77, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.612×** | -5.9 | 2e-07 | 37/46 (SNU-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.615×** | -5.8 | 3e-07 | 39/45 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.676×** | -5.6 | 1e-06 | 33/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.630×** | -5.5 | 1e-06 | 33/46 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.637×** | -5.2 | 7e-06 | 37/45 (A549, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.649×** | -5.2 | 7e-06 | 29/45 (A-427, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.648×** | -5.0 | 2e-05 | 27/45 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.609×** | -5.0 | 2e-05 | 30/46 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.751×** | -4.6 | 1e-04 | 29/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.692×** | -4.4 | 3e-04 | 28/45 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.682×** | -4.2 | 5e-04 | 26/45 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -4.2 | 7e-04 | 25/45 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.25 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 190 | 7 (6 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.25× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.72× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -15.4) |
| [[A-427 (line)]] | wt | 468 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -28.0) |
| [[H4 (line)]] | wt | 154 | 1 | 8 (4 ⚠) | [[Auranofin (drug)]] 5 µM 4.09× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 115 | 2 (2 ⚠) | 6 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.159× (z -17.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.316× (z -11.2) |
| [[LS 180 (line)]] | wt | 95.1 | 1 (1 ⚠) | 7 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.0938× (z -19.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.271× (z -11.1) |
| [[A498 (line)]] | wt | 231 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.101× (z -17.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.0) |
| [[A-172 (line)]] | wt | 161 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.148× (z -15.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.339× (z -8.9) |
| [[A549 (line)]] | wt | 116 | 2 (2 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.284× (z -12.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.422× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 193 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 108 | 2 (2 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.192× (z -15.0) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -10.2) |
| [[HT-29 (line)]] | alt | 87.4 | 2 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.30× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.206× (z -12.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.0) |
| [[KATO III (line)]] | alt | 174 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 0.05 µM 0.0799× (z -12.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 347 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -20.0) |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -16.3) |
| [[SNU-1 (line)]] | wt | 110 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.127× (z -13.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.131× (z -13.1) |
| [[HCT15 (line)]] | alt | 316 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.0) |
| [[Hs 766T (line)]] | wt | 61.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.4) |
| [[RKO (line)]] | wt | 174 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -12.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -11.8) |
| [[SW48 (line)]] | wt | 162 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.165× (z -11.2) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.372× (z -8.6) |
| [[HOP62 (line)]] | alt | 416 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 73.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.359× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW1417 (line)]] | alt | 101 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 91.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.306× (z -11.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -9.5) |
| [[COLO 205 (line)]] | alt | 83.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.128× (z -11.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HS-578T (line)]] | alt | 93.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 64.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.187× (z -15.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 42.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.97× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 190 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 55.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.311× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[hTERT-HPNE (line)]] | wt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 85.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 150 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG2]] | +0.89 | +0.89 / +0.85 | both halves | 7e-06 | STRING 757 |
| [[CENPK]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 | STRING 531 |
| [[FANCA]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[POLE]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCI]] | +0.85 | +0.82 / +0.84 | both halves | 7e-06 | STRING 633 |
| [[MELK]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 933 |
| [[EXO1]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 | STRING 788 |
| [[POLQ]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[SPC25]] | +0.84 | +0.83 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 699 |
| [[TK1]] | +0.84 | +0.80 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 914 |
| [[MCM8]] | +0.83 | +0.79 / +0.86 | both halves | 7e-06 | pathway: G1/S Transition; STRING 448 |
| [[FANCB]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD3B]] | B | TLCD3B activity raises RRM2's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without TLCD3B | 0.091 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises RRM2's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[E2F8]] | C | E2F8 activity raises RRM2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.97× lower at baseline in the lines without E2F8 | 0.017 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent; co-absent with the target |
| [[TCF19]] | C | TCF19 activity raises RRM2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 3.33× lower at baseline in the lines without TCF19 | 0.027 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[DSCC1]] | C | DSCC1 activity raises RRM2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without DSCC1 | 0.051 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises RRM2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without AURKB | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CLSPN]] | C | CLSPN activity raises RRM2's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 3.83× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises RRM2's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.85× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[SHMT1]] | C | SHMT1 activity raises RRM2's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.25× lower at baseline in the lines without SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises RRM2's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.95× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Auranofin (drug)]] 5 µM | C | RRM2 activity lowers the cells' numbers under Auranofin 5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.64× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[BAY1125976 (drug)]] 5 µM | C | RRM2 activity lowers the cells' numbers under BAY1125976 5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.89× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Adenosine (drug)]] 5 µM | C | RRM2 activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.21× the cells of the other lines | 0.048 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 0.5 µM | C | RRM2 activity lowers the cells' numbers under Digitoxin 0.5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.68× the cells of the other lines | 0.072 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | C | RRM2 activity lowers the cells' numbers under Vinblastine (sulfate) 0.05 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.30× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | C | RRM2 activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.25× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Binimetinib (drug)]] 0.05 µM | C | RRM2 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 0.73× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM | C | RRM2 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 0.05 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.28× the cells of the other lines | 0.091 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Capmatinib (drug)]] 5 µM | C | RRM2 activity raises the cells' numbers under Capmatinib 5 µM (protects the cells) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 0.67× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 5 µM | C | RRM2 activity lowers the cells' numbers under Peretinoin 5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.35× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.865). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.5, -46.0); signed map (-38.9, -43.8). **Vector** length 170, 68.1% of its response variance represented; |z| ≥ 3 in 1,827 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40); *Synthesis of DNA* (reactome, mean cos +0.67 to 37).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.7 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | +7.3 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +4.9 | +5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +3.3 |
|  | [[Methotrexate (drug)]] 5 µM |  | +3.9 | +2.2 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +3.5 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +3.1 | +2.1 |
|  | [[Oxaliplatin (drug)]] 0.5 µM |  | +3.1 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -13.1 | -12.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -10.6 | -10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | -8.0 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.8 | -7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.9 | -5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -6.5 | -6.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.4 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.1 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | ribonucleotide reductase regulatory subunit M2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,120,698-10,211,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25102; previously C2orf48 |
| Gene groups (HGNC) | Ribonucleotide reductase subunits |
| Hallmark sets | MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 8 pathways, smallest: G1/S-Specific Transcription; Interconversion of nucleotide di- and triphosphates; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [P31350](https://www.uniprot.org/uniprotkb/P31350) (Ribonucleoside-diphosphate reductase subunit M2):

> Part of the ribonucleotide reductase (RNR) complex composed of a catalytic large alpha subunit (RRM1/RR1) and a small beta subunit (RRM2/RR2) required for DNA synthesis. The active form is an alpha2beta2 heterotetramer in which the RR1-containing subunits (alpha2) catalyze reduction of ribonucleotides to deoxyribonucleotides, while the RRM2-containing subunits (beta2) provide the diferric-tyrosyl radical cofactor required for catalysis and radical transfer. Mechanistically, RRM2-containing …

**Summary**, from NCBI Gene [6241](https://www.ncbi.nlm.nih.gov/gene/6241):

> This gene encodes one of two non-identical subunits for ribonucleotide reductase. This reductase catalyzes the formation of deoxyribonucleotides from ribonucleotides. Synthesis of the encoded protein (M2) is regulated in a cell-cycle dependent fashion. Transcription from this gene can initiate from alternative promoters, which results in two isoforms that differ in the lengths of their N-termini. Related pseudogenes have been identified on chromosomes 1 and X. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:10452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10452) · Entrez [6241](https://www.ncbi.nlm.nih.gov/gene/6241) · UniProt [P31350](https://www.uniprot.org/uniprotkb/P31350) · Ensembl [ENSG00000171848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171848)

## Data

Gene col 10173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10173); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10173]; `tensor/DDL_lfc|DDL_z.npy` [10173]; `embed/gene_vectors.npy` [10173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10173 or target_col == 10173). Every well: [[RRM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
