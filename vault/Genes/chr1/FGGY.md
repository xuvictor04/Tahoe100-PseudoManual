---
symbol: "FGGY"
type: "gene"
col: 10257
ensembl_id: "ENSG00000172456"
name: "FGGY carbohydrate kinase domain containing"
location: "1p32.1"
module: 200
arm: "+"
pooled_cpm: 79.56
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 40
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# FGGY

*FGGY carbohydrate kinase domain containing* — 1p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +5.8, q 3e-06, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (18 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.302× (z -13.7, q 6e-40, down in 44 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.344× (z -12.7, q 9e-35, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIG1]] (+0.66, fdr 9e-06), [[WWOX]] (+0.64, fdr 1e-05), [[BABAM2]] (+0.62, fdr 7e-06); moves opposite to [[MFSD8]] (-0.57, fdr 3e-05), [[GLUD1P3]] (-0.56, fdr 4e-05), [[RAB5B]] (-0.56, fdr 3e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.8 | 3e-06 | 34/47 (A-172, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 4e-05 | 35/48 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 0.004 | 24/47 (A-172, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.009 | 24/46 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.024 | 24/47 (HepG2/C3A, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.39×** | +3.5 | 0.045 | 20/49 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.069 | 25/46 (HepG2/C3A, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.32× | +3.2 | 0.10 | 20/47 (AsPC-1, A-172, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.13 | 18/47 (NCI-H1792, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.302×** | -13.7 | 6e-40 | 44/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.328×** | -13.3 | 1e-37 | 45/47 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.329×** | -13.2 | 1e-37 | 45/47 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.344×** | -12.7 | 9e-35 | 45/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.348×** | -12.6 | 4e-34 | 42/47 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.515×** | -11.2 | 6e-27 | 41/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.391×** | -10.8 | 4e-25 | 42/45 (HepG2/C3A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.423×** | -10.3 | 8e-23 | 41/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.582×** | -9.1 | 5e-18 | 36/47 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.458×** | -8.9 | 2e-17 | 37/47 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.461×** | -8.9 | 4e-17 | 38/47 (PANC-1, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.482×** | -8.7 | 2e-16 | 42/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.480×** | -8.4 | 2e-15 | 32/41 (NCI-H23, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.475×** | -8.4 | 3e-15 | 43/47 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -6.9 | 2e-10 | 31/49 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -6.9 | 3e-10 | 40/48 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.700×** | -6.0 | 7e-08 | 44/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.389×** | -5.9 | 1e-07 | 33/47 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.687×** | -4.5 | 2e-04 | 33/47 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.783×** | -4.1 | 1e-03 | 27/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.664×** | -3.7 | 0.005 | 27/47 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.666×** | -3.7 | 0.005 | 26/46 (NCI-H23, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.657×** | -3.6 | 0.006 | 28/47 (A-427, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 126 | 0 | 19 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0718× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.142× (z -17.4) |
| [[PANC-1 (line)]] | alt | 159 | 0 | 18 (12 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -20.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.161× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 68.3 | 0 | 16 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.182× (z -15.0) |
| [[LS 180 (line)]] | wt | 121 | 0 | 13 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.177× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 58.0 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.9) |
| [[J82 (line)]] | alt | 97.9 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.220× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 10 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0521× (z -25.3) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.315× (z -10.3) |
| [[SW480 (line)]] | alt | 92.3 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.217× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 99.5 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 96.2 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.9) |
| [[A549 (line)]] | wt | 69.2 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 234 | 0 | 8 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -16.5) |
| [[COLO 205 (line)]] | alt | 92.2 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -22.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 87.4 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0637× (z -19.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.303× (z -8.9) |
| [[KATO III (line)]] | alt | 51.5 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0902× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.300× (z -9.4) |
| [[LoVo (line)]] | wt | 61.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0779× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.228× (z -14.6) |
| [[A-427 (line)]] | wt | 93.4 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 89.7 | 0 | 6 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 64.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.244× (z -9.5) |
| [[RKO (line)]] | wt | 72.6 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -12.1) |
| [[SW1417 (line)]] | alt | 70.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.261× (z -10.0) |
| [[C32 (line)]] | wt | 104 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -8.9) |
| [[HT-29 (line)]] | alt | 50.3 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.6) |
| [[SNU-423 (line)]] | alt | 77.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.0) |
| [[A-172 (line)]] | wt | 63.2 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +14.7) ⚠ cell-cycle shift, explains ~62% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.7) |
| [[A498 (line)]] | wt | 68.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.276× (z -8.8) |
| [[Hs 766T (line)]] | wt | 65.9 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.243× (z -10.4) |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0837× (z -11.4) ⚠ toxic · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.0992× (z -10.2) |
| [[HCT15 (line)]] | alt | 71.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 71.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -14.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.248× (z -10.0) |
| [[BT-474 (line)]] | alt | 37.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +13.5) ⚠ cell-cycle shift, explains ~62% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.408× (z -8.5) |
| [[H4 (line)]] | wt | 69.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2030 (line)]] | alt | 75.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.256× (z -8.7) |
| [[SW 1088 (line)]] | alt | 131 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0684× (z -9.9) |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -9.0) |
| [[SW48 (line)]] | wt | 45.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.129× (z -10.8) |
| [[C-33 A (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -9.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.275× (z -9.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -11.4) |
| [[SHP-77 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIG1]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[WWOX]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[BABAM2]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SERBP1]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CLYBL]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC01473]] | +0.58 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[RAD51B]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PRKN]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[GTDC1]] | +0.55 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[IQCH]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | -0.57 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[GLUD1P3]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RAB5B]] | -0.56 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[C1orf54]] | -0.52 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[DENND10]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RNF139-DT]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[CCDC168]] | -0.50 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZFYVE21]] | -0.50 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[MXD4]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[EGFL8]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[METTL21EP-1]] | -0.50 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[FGD1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FGGY's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.6, 31.4); signed map (9.5, -12.0). **Vector** length 80.6, 26.7% of its response variance represented; |z| ≥ 3 in 1,555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.5 | -8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.0 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -10.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | FGGY carbohydrate kinase domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.1 — chr1:59,296,638-59,810,647 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10986 |
| Gene groups (HGNC) | Carbohydrate kinases; FGGY kinase family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C11](https://www.uniprot.org/uniprotkb/Q96C11) (FGGY carbohydrate kinase domain-containing protein):

> Catalyzes ATP-dependent phosphorylation of D-ribulose at C-5 to form D-ribulose 5-phosphate. Postulated to function in a metabolite repair mechanism by preventing toxic accumulation of free D-ribulose formed by non-specific phosphatase activities. Alternatively, may play a role in regulating D-ribulose 5-phosphate recycling in the pentose phosphate pathway. Can phosphorylate ribitol with low efficiency.

**Summary**, from NCBI Gene [55277](https://www.ncbi.nlm.nih.gov/gene/55277):

> This gene encodes a protein that phosphorylates carbohydrates such as ribulose, ribitol, and L-arabinitol. Genome-wide association studies in some populations have found an association between polymorphisms in this gene and sporadic amyotrophic lateral sclerosis, but studies of other populations have not been able to replicate this association. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:25610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25610) · Entrez [55277](https://www.ncbi.nlm.nih.gov/gene/55277) · UniProt [Q96C11](https://www.uniprot.org/uniprotkb/Q96C11) · Ensembl [ENSG00000172456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172456)

## Data

Gene col 10257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10257); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10257]; `tensor/DDL_lfc|DDL_z.npy` [10257]; `embed/gene_vectors.npy` [10257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10257 or target_col == 10257). Every well: [[FGGY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGGY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
