---
symbol: "HIBADH"
type: "gene"
col: 2713
ensembl_id: "ENSG00000106049"
name: "3-hydroxyisobutyrate dehydrogenase"
location: "7p15.2"
module: 65
arm: "+"
pooled_cpm: 158.24
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# HIBADH

*3-hydroxyisobutyrate dehydrogenase* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +11.6, q 2e-28, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.620× (z -12.0, q 2e-30, down in 38 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.699× (z -9.0, q 3e-17, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBE1]] (+0.57, fdr 1e-05), [[SLC35A1]] (+0.57, fdr 2e-05), [[KIF3A]] (+0.56, fdr 1e-05); moves opposite to [[MC1R]] (-0.55, fdr 4e-05), [[REXO1]] (-0.55, fdr 4e-05), [[PCF11]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +11.6 | 2e-28 | 37/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +8.1 | 1e-13 | 34/49 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.4 | 3e-11 | 30/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +7.3 | 4e-11 | 31/48 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +6.2 | 6e-08 | 27/48 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +5.9 | 4e-07 | 28/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +5.8 | 6e-07 | 32/49 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +4.9 | 7e-05 | 24/50 (SNU-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.14× | +4.6 | 3e-04 | 12/48 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +4.4 | 5e-04 | 23/49 (hTERT-HPNE, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.008 | 20/47 (HOP62, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.019 | 17/50 (SNU-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +3.5 | 0.023 | 11/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.4 | 0.025 | 18/48 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.2 | 0.048 | 8/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.0 | 0.092 | 4/48 (C32, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.620×** | -12.0 | 2e-30 | 38/48 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.634×** | -10.6 | 9e-24 | 33/45 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.665×** | -10.3 | 2e-22 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -9.2 | 7e-18 | 33/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -9.0 | 3e-17 | 36/48 (SW480, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.700×** | -9.0 | 3e-17 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.711×** | -8.6 | 8e-16 | 39/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.723×** | -8.1 | 3e-14 | 35/49 (Panc 03.27, SW1417, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.718×** | -8.0 | 8e-14 | 31/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.803×** | -7.8 | 4e-13 | 25/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.739×** | -7.6 | 2e-12 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.735×** | -7.4 | 5e-12 | 26/44 (Panc 03.27, A498, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -7.4 | 7e-12 | 33/48 (SW48, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -6.7 | 7e-10 | 32/48 (CFPAC-1, SW48, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.794×** | -5.8 | 3e-07 | 29/48 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.688×** | -4.9 | 3e-05 | 28/48 (SW1417, C32, …) | top dose only | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.864× | -3.7 | 0.007 | 13/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.784×** | -3.2 | 0.034 | 14/47 (SW48, C32, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.788×** | -3.1 | 0.040 | 15/48 (SW1417, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.884× | -3.1 | 0.044 | 16/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.886× | -3.0 | 0.052 | 9/48 (CFPAC-1, RPMI-7951, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.919× | -3.0 | 0.053 | 10/48 (A549, NCI-H2347, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.803×** | -2.9 | 0.073 | 10/48 (SW1417, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.891× | -2.9 | 0.073 | 12/48 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.889× | -2.8 | 0.078 | 12/48 (PANC-1, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 163 | 0 | 10 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -22.1) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW48 (line)]] | wt | 239 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -11.2) |
| [[SW1417 (line)]] | alt | 242 | 0 | 9 (7 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.449× (z -12.0) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.522× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 167 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 333 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -20.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW480 (line)]] | alt | 122 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.371× (z -16.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.486× (z -11.8) |
| [[A-172 (line)]] | wt | 192 | 1 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.68× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -16.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 157 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -20.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[LS 180 (line)]] | wt | 113 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.84× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -24.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[C32 (line)]] | wt | 112 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -11.4) ⚠ cell-cycle shift, explains ~71% of this change |
| [[HS-578T (line)]] | alt | 79.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[AsPC-1 (line)]] | alt | 331 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.5) ⚠ cell-cycle shift, explains ~71% of this change | [[Lonafarnib (drug)]] 5 µM 0.266× (z -8.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.479× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.509× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 66.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -13.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SHP-77 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 120 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[CFPAC-1 (line)]] | alt | 138 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.98× (z +10.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.364× (z -11.2) |
| [[COLO 205 (line)]] | alt | 97.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 184 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -10.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[HOP62 (line)]] | alt | 86.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.11× (z +11.8) | — |
| [[LoVo (line)]] | wt | 181 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.466× (z -11.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 77.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H2030 (line)]] | alt | 271 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[Panc 03.27 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 201 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.1) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW 900 (line)]] | alt | 97.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.413× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -9.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 83.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[J82 (line)]] | alt | 97.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.450× (z -9.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.470× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 126 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.69× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 176 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.2) | — |
| [[A-427 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 169 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 282 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 216 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBE1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SLC35A1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[KIF3A]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ATG4C]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TPD52]] | +0.54 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[MTX2]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ANAPC4]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ZCRB1]] | +0.52 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[SGK3]] | +0.52 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[GPR160]] | +0.51 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[ABHD10]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[CMC1]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MC1R]] | -0.55 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[REXO1]] | -0.55 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PCF11]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[DMWD]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[WNK4]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CHMP6]] | -0.50 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[DMPK]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[DNAH1]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZNF629]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.49 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[EIF2B5]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HIBADH's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers HIBADH's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.5, -10.8); signed map (-32.9, -8.2). **Vector** length 116, 34.6% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +8.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.5 | +4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.4 | +2.6 |
|  | [[Bexarotene (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.9 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -6.4 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -5.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -5.1 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxyisobutyrate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,525,442-27,662,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NS5ATP1 |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 2 pathways, smallest: Branched-chain amino acid catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

UniProt [P31937](https://www.uniprot.org/uniprotkb/P31937) carries no function annotation.

**Summary**, from NCBI Gene [11112](https://www.ncbi.nlm.nih.gov/gene/11112):

> This gene encodes a mitochondrial 3-hydroxyisobutyrate dehydrogenase enzyme. The encoded protein plays a critical role in the catabolism of L-valine by catalyzing the oxidation of 3-hydroxyisobutyrate to methylmalonate semialdehyde. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:4907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4907) · Entrez [11112](https://www.ncbi.nlm.nih.gov/gene/11112) · UniProt [P31937](https://www.uniprot.org/uniprotkb/P31937) · Ensembl [ENSG00000106049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106049)

## Data

Gene col 2713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2713); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2713]; `tensor/DDL_lfc|DDL_z.npy` [2713]; `embed/gene_vectors.npy` [2713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2713 or target_col == 2713). Every well: [[HIBADH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIBADH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
