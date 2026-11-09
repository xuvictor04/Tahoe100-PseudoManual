---
symbol: "UBE2O"
type: "gene"
col: 10666
ensembl_id: "ENSG00000175931"
name: "ubiquitin conjugating enzyme E2 O"
location: "17q25.1"
module: 164
arm: "+"
pooled_cpm: 144.26
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# UBE2O

*ubiquitin conjugating enzyme E2 O* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.99× (z +10.0, q 6e-21, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.303× (z -20.1, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -11.0, q 6e-26, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPC3]] (+0.77, fdr 7e-06), [[INSIG2]] (+0.76, fdr 7e-06), [[MMS19]] (+0.76, fdr 7e-06); moves opposite to [[ZNF655]] (-0.69, fdr 7e-06), [[POGLUT1]] (-0.69, fdr 2e-05), [[PARVA]] (-0.69, fdr 7e-06).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01583]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.99×** | +10.0 | 6e-21 | 47/49 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +9.0 | 5e-17 | 43/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.1 | 3e-07 | 35/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.6 | 4e-06 | 30/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.2 | 3e-05 | 32/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 31/48 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 1e-03 | 27/48 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.007 | 24/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.2 | 0.079 | 22/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.20× | +3.2 | 0.083 | 21/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.092 | 21/49 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +3.1 | 0.092 | 23/48 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.092 | 20/48 (NCI-H2347, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.303×** | -20.1 | 0e+00 | 42/44 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.334×** | -19.2 | 0e+00 | 48/49 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.361×** | -16.5 | 0e+00 | 44/45 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -11.0 | 6e-26 | 38/48 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.687×** | -6.3 | 3e-08 | 29/48 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.2 | 5e-08 | 35/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -5.9 | 2e-07 | 31/48 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -5.5 | 2e-06 | 32/47 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -5.2 | 1e-05 | 32/47 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.808×** | -4.8 | 7e-05 | 26/48 (Panc 03.27, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.768×** | -4.2 | 0.001 | 28/48 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.768×** | -4.2 | 0.001 | 30/48 (LS 180, RPMI-7951, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -4.1 | 0.002 | 27/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.784×** | -3.9 | 0.004 | 27/49 (A498, HOP62, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.790×** | -3.8 | 0.006 | 28/49 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.791×** | -3.8 | 0.006 | 26/48 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.799×** | -3.6 | 0.011 | 23/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.809×** | -3.4 | 0.021 | 23/49 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.022 | 21/48 (J82, PANC-1, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.865× | -3.3 | 0.023 | 9/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 176 | 1 | 7 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.01× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0846× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -20.1) |
| [[C32 (line)]] | wt | 233 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.6) |
| [[SW480 (line)]] | alt | 104 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 159 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -15.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 75.2 | 4 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.49× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -25.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 194 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.414× (z -10.1) |
| [[A549 (line)]] | wt | 257 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.318× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.330× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 209 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.16× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 147 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0450× (z -33.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.5) |
| [[HOP62 (line)]] | alt | 255 | 1 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.85× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 159 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 250 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -16.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.4) |
| [[H4 (line)]] | wt | 258 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.3) |
| [[HS-578T (line)]] | alt | 179 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.1) |
| [[SNU-423 (line)]] | alt | 232 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.315× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 298 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -14.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 163 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -17.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 114 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 149 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 96.9 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.80× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 131 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.14× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 99.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -13.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 91.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -9.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 96.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -16.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -18.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 128 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.94× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -13.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 91.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 91.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 109 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 202 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC3]] | +0.77 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.76 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[MMS19]] | +0.76 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.75 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.74 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.72 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.72 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.72 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.71 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.71 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.71 | +0.75 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.69 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[POGLUT1]] | -0.69 | -0.75 / -0.47 | both halves | 2e-05 |  |
| [[PARVA]] | -0.69 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ST7L]] | -0.68 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[ERMAP]] | -0.67 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[PPP3CB-AS1]] | -0.66 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[FKRP]] | -0.64 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[ZNF644]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ARMCX4]] | -0.64 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.63 | -0.69 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01583]] | B | LINC01583 activity raises UBE2O's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without LINC01583 | 0.020 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[A1BG]] | B | A1BG activity raises UBE2O's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without A1BG | 0.068 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[TMEM255B]] | B | TMEM255B activity raises UBE2O's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without TMEM255B | 0.094 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[SLC2A1]], [[TCAF2]] | C | SLC2A1, TCAF2 activity raises UBE2O's level | lines that do not express SLC2A1, TCAF2 (4) vs lines expressing them (46) | 1.67× lower at baseline in the lines without SLC2A1, TCAF2 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[SLC6A6]] | C | SLC6A6 activity raises UBE2O's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without SLC6A6 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.836). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.2, -16.0); signed map (-36.5, 23.1). **Vector** length 138, 49.7% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.8 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +7.5 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +9.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.8 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.0 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.8 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -16.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.3 | -3.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.1 | -4.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.0 | -3.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,389,456-76,453,152 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E2-230K |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2; Atypical E3 ubiquitin ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0C9](https://www.uniprot.org/uniprotkb/Q9C0C9) ((E3-independent) E2 ubiquitin-conjugating enzyme):

> E2/E3 hybrid ubiquitin-protein ligase that displays both E2 and E3 ligase activities and mediates monoubiquitination of target proteins. Negatively regulates TRAF6-mediated NF-kappa-B activation independently of its E2 activity. Acts as a positive regulator of BMP7 signaling by mediating monoubiquitination of SMAD6, thereby regulating adipogenesis. Mediates monoubiquitination at different sites of the nuclear localization signal (NLS) of BAP1, leading to cytoplasmic retention of BAP1. Also able …

**Summary**, from NCBI Gene [63893](https://www.ncbi.nlm.nih.gov/gene/63893):

> Enables ubiquitin conjugating enzyme activity and ubiquitin protein ligase activity. Involved in positive regulation of BMP signaling pathway; protein ubiquitination; and retrograde transport, endosome to Golgi. Located in cytoplasm and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29554) · Entrez [63893](https://www.ncbi.nlm.nih.gov/gene/63893) · UniProt [Q9C0C9](https://www.uniprot.org/uniprotkb/Q9C0C9) · Ensembl [ENSG00000175931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175931)

## Data

Gene col 10666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10666); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10666]; `tensor/DDL_lfc|DDL_z.npy` [10666]; `embed/gene_vectors.npy` [10666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10666 or target_col == 10666). Every well: [[UBE2O — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2O.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
