---
symbol: "UBR2"
type: "gene"
col: 355
ensembl_id: "ENSG00000024048"
name: "ubiquitin protein ligase E3 component n-recognin 2"
location: "6p21.1"
module: 187
arm: "+"
pooled_cpm: 171.8
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# UBR2

*ubiquitin protein ligase E3 component n-recognin 2* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.73× (z +12.9, q 1e-35, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.390× (z -21.8, q 0e+00, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.666× (z -5.3, q 8e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE4B]] (+0.70, fdr 7e-06), [[TNKS]] (+0.66, fdr 7e-06), [[ABCD4]] (+0.66, fdr 1e-05); moves opposite to [[VMA21]] (-0.60, fdr 1e-05), [[SYNCRIP]] (-0.57, fdr 1e-05), [[ASMTL-AS1]] (-0.56, fdr 1e-05).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PTP4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +12.9 | 1e-35 | 46/48 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +12.5 | 4e-33 | 43/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +10.5 | 2e-23 | 29/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +9.0 | 2e-17 | 42/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +7.5 | 5e-12 | 28/48 (RKO, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 2e-08 | 38/49 (A-427, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.61×** | +6.2 | 4e-08 | 41/49 (Panc 03.27, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.1 | 6e-08 | 35/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.8 | 4e-07 | 29/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +5.3 | 8e-06 | 25/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 6e-04 | 23/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 21/47 (LoVo, J82, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 21/49 (A-427, HepG2/C3A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 25/47 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.028 | 18/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.054 | 21/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.079 | 14/48 (RKO, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.390×** | -21.8 | 0e+00 | 44/45 (CFPAC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -20.4 | 0e+00 | 41/44 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.405×** | -17.9 | 0e+00 | 47/49 (COLO 205, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -12.4 | 4e-33 | 43/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -10.4 | 4e-23 | 45/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.778×** | -8.9 | 5e-17 | 27/49 (A549, SNU-423, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.666×** | -5.3 | 8e-06 | 31/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.685×** | -5.0 | 5e-05 | 29/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.688×** | -4.9 | 5e-05 | 30/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.818×** | -4.9 | 6e-05 | 25/48 (LoVo, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.692×** | -4.8 | 7e-05 | 27/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.814×** | -4.8 | 9e-05 | 26/48 (KATO III, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.821×** | -4.6 | 2e-04 | 25/47 (J82, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.796×** | -4.5 | 2e-04 | 28/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.845× | -3.9 | 0.004 | 20/48 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.870× | -3.5 | 0.016 | 15/48 (KATO III, A-172, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.863× | -3.4 | 0.022 | 12/49 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.032 | 21/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.875× | -3.2 | 0.044 | 9/48 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.917× | -3.1 | 0.057 | 2/48 (A498, NCI-H661) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.065 | 14/49 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.889× | -3.0 | 0.073 | 8/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.884× | -2.9 | 0.095 | 10/48 (A498, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 177 | 7 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 201 | 5 (3 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -24.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 152 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 146 | 5 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.14× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 166 | 4 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 107 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -17.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 149 | 3 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.93× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -19.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 301 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -18.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -20.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 870 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -24.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 217 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 187 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -16.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 152 | 3 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.18× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 109 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -15.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -16.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 157 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 190 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 264 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.168× (z -20.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 217 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -14.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -17.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 282 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -15.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -17.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 120 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 137 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.2) | [[Lonafarnib (drug)]] 5 µM 0.0961× (z -16.0) ⚠ toxic |
| [[H4 (line)]] | wt | 224 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 261 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -20.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 146 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 135 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.73× (z +17.9) | — |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.99× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -20.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 166 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -11.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 123 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.60× (z +13.8) | — |
| [[J82 (line)]] | alt | 99.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.463× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -13.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 113 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.13× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -13.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -16.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 180 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.1) | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE4B]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 | STRING 417 |
| [[TNKS]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ABCD4]] | +0.66 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[CIR1]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 975 |
| [[EAPP]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[BSDC1]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MRPL43]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TRIM23]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | same gene group |
| [[ANAPC1P2]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RNF181]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 | same gene group |
| [[SNRNP48]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[SYNCRIP]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ASMTL-AS1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[WDR77]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[RBM12]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[VARS1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GGACT]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TRNT1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTP4A3]] | B | PTP4A3 activity lowers UBR2's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without PTP4A3 | 0.095 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[ZMAT5]] | C | ZMAT5's natural level weakens UBR2's drug response | ZMAT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.35; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.3, -11.7); signed map (-21.7, 4.2). **Vector** length 131, 46.5% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.4 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +7.5 |
|  | [[NG25 (drug)]] 5 µM |  | +5.3 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +6.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.4 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.0 | -21.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.3 | -12.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.2 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.1 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3 component n-recognin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,564,029-42,693,505 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA49A4.1, dJ392M17.3, KIAA0349; previously C6orf133 |
| Gene groups (HGNC) | Ubiquitin protein ligase E3 component n-recognins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWV8](https://www.uniprot.org/uniprotkb/Q8IWV8) (E3 ubiquitin-protein ligase UBR2):

> E3 ubiquitin-protein ligase which is a component of the N-end rule pathway. Recognizes and binds to proteins bearing specific N-terminal residues (N-degrons) that are destabilizing according to the N-end rule, leading to their ubiquitination and subsequent degradation. Recognizes both type-1 and type-2 N-degrons, containing positively charged amino acids (Arg, Lys and His) and bulky and hydrophobic amino acids, respectively. Does not ubiquitinate proteins that are acetylated at the N-terminus. …

**Summary**, from NCBI Gene [23304](https://www.ncbi.nlm.nih.gov/gene/23304):

> Enables L-leucine binding activity and ubiquitin protein ligase activity. Involved in several processes, including cellular response to L-leucine; protein K63-linked ubiquitination; and regulation of signal transduction. Predicted to be located in cytosol. Predicted to be part of ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21289) · Entrez [23304](https://www.ncbi.nlm.nih.gov/gene/23304) · UniProt [Q8IWV8](https://www.uniprot.org/uniprotkb/Q8IWV8) · Ensembl [ENSG00000024048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000024048)

## Data

Gene col 355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 355); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 355]; `tensor/DDL_lfc|DDL_z.npy` [355]; `embed/gene_vectors.npy` [355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 355 or target_col == 355). Every well: [[UBR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
