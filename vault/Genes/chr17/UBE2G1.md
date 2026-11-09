---
symbol: "UBE2G1"
type: "gene"
col: 5312
ensembl_id: "ENSG00000132388"
name: "ubiquitin conjugating enzyme E2 G1"
location: "17p13.2"
module: 163
arm: "+"
pooled_cpm: 127.19
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# UBE2G1

*ubiquitin conjugating enzyme E2 G1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.05× (z +12.9, q 2e-35, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.01× (z +12.5, q 2e-33, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.391× (z -16.9, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.616× (z -8.8, q 3e-16, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPK2]] (+0.77, fdr 7e-06), [[FOXK2]] (+0.73, fdr 7e-06), [[RNF38]] (+0.72, fdr 7e-06); moves opposite to [[TRMT13]] (-0.67, fdr 1e-05), [[AIMP1]] (-0.66, fdr 1e-05), [[MYSM1]] (-0.65, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PYROXD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +12.9 | 2e-35 | 45/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +12.5 | 2e-33 | 44/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +11.1 | 4e-26 | 42/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +10.1 | 1e-21 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +9.5 | 3e-19 | 44/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +9.3 | 1e-18 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +8.6 | 5e-16 | 41/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +8.1 | 5e-14 | 38/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +7.7 | 8e-13 | 39/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +7.3 | 2e-11 | 34/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +7.2 | 4e-11 | 35/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 7e-08 | 35/48 (C32, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +5.6 | 8e-07 | 34/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +5.4 | 2e-06 | 33/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.9 | 5e-05 | 33/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 1e-04 | 28/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.001 | 28/49 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.391×** | -16.9 | 0e+00 | 47/49 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -16.5 | 0e+00 | 39/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.444×** | -13.6 | 1e-39 | 40/45 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -8.8 | 3e-16 | 36/48 (AN3 CA, A-427, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.727×** | -5.8 | 9e-07 | 33/48 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -5.0 | 5e-05 | 22/48 (Hs 766T, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.770×** | -4.5 | 4e-04 | 30/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.4 | 9e-04 | 29/48 (A-172, A-427, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~4% of this change | **0.824×** | -3.5 | 0.027 | 22/48 (KATO III, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.832×** | -3.3 | 0.046 | 18/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.046 | 20/47 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.889× | -3.0 | 0.12 | 13/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -3.0 | 0.12 | 5/48 (RKO, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 134 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -14.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 101 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.89× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 154 | 7 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.57× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -21.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 191 | 6 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.42× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -17.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 111 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -15.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 94.4 | 5 (2 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.30× (z +14.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -12.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 60.8 | 7 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.71× (z +13.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 140 | 6 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.80× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.56× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 119 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.8) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -11.0) |
| [[C32 (line)]] | wt | 105 | 3 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 11.0× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 115 | 3 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 96.6 | 5 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.58× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 169 | 1 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.50× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.469× (z -8.5) |
| [[H4 (line)]] | wt | 75.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.22× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 66.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.39× (z +10.7) ⚠ toxic | [[Selinexor (drug)]] 5 µM 0.515× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 194 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.30× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 94.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.40× (z +9.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -9.8) |
| [[SHP-77 (line)]] | alt | 137 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.45× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 108 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.97× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 117 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.28× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -15.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 193 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0697× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 157 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -14.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 175 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -16.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 111 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.51× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -15.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 146 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.40× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -18.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -10.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 140 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 5.53× (z +10.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.474× (z -8.6) |
| [[SW 1088 (line)]] | alt | 83.7 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0729× (z -9.1) ⚠ transcription drop · without an alert: [[Sunitinib (drug)]] 0.05 µM 0.0840× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.4) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 81.7 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.154× (z -8.8) |
| [[HOP62 (line)]] | alt | 88.0 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.36× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 77.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.51× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0680× (z -15.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[RNF38]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SAP130]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MFSD14B]] | +0.69 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[PPP2R5E]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ABHD12]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[CYTH3]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[UBE2R2]] | +0.66 | +0.70 / +0.57 | both halves | 9e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 431 |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.67 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[AIMP1]] | -0.66 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.65 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.64 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[DARS1]] | -0.64 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.63 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[TAF9]] | -0.62 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[ARCN1]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[FCF1]] | -0.61 | -0.75 / -0.44 | both halves | 3e-05 |  |
| [[ZC3H11A]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LINC00174]] | -0.60 | -0.67 / -0.37 | both halves | 7e-05 |  |
| [[STAMBP]] | -0.60 | -0.67 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYROXD2]] | B | PYROXD2 activity lowers UBE2G1's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.56× higher at baseline in the lines without PYROXD2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.5, -5.8); signed map (-41.8, 0.1). **Vector** length 119, 44.6% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.6 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.4 | +11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.1 | +4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | +3.7 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | -0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -14.0 | -8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -12.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.9 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.8 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,269,259-4,366,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBC7; previously UBE2G |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62253](https://www.uniprot.org/uniprotkb/P62253) (Ubiquitin-conjugating enzyme E2 G1):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-48'-, as well as 'Lys-63'-linked polyubiquitination. May be involved in degradation of muscle-specific proteins. Mediates polyubiquitination of CYP3A4.

**Summary**, from NCBI Gene [7326](https://www.ncbi.nlm.nih.gov/gene/7326):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family and catalyzes the covalent attachment of ubiquitin to other proteins. The protein may be involved in …

**Accessions** — [HGNC:12482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12482) · Entrez [7326](https://www.ncbi.nlm.nih.gov/gene/7326) · UniProt [P62253](https://www.uniprot.org/uniprotkb/P62253) · Ensembl [ENSG00000132388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132388)

## Data

Gene col 5312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5312); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5312]; `tensor/DDL_lfc|DDL_z.npy` [5312]; `embed/gene_vectors.npy` [5312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5312 or target_col == 5312). Every well: [[UBE2G1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2G1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
