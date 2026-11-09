---
symbol: "ECPAS"
type: "gene"
col: 5907
ensembl_id: "ENSG00000136813"
name: "Ecm29 proteasome adaptor and scaffold"
location: "9q31.3"
module: 18
arm: "+"
pooled_cpm: 203.47
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ECPAS

*Ecm29 proteasome adaptor and scaffold* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.24× (z +17.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.207× (z -34.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDS5A]] (+0.62, fdr 7e-06), [[MAP4]] (+0.61, fdr 7e-06), [[UBE2Q2]] (+0.60, fdr 2e-05); moves opposite to [[INIP]] (-0.57, fdr 1e-05), [[NME7]] (-0.55, fdr 2e-05), [[NFKBIE]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.24×** | +17.6 | 0e+00 | 47/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.20×** | +16.2 | 0e+00 | 47/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.90×** | +14.0 | 5e-42 | 46/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +9.5 | 4e-19 | 42/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.3 | 1e-14 | 32/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +7.3 | 3e-11 | 42/49 (MIA PaCa-2, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 1e-09 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.0 | 1e-07 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 1e-06 | 29/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.3 | 6e-06 | 20/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.1 | 2e-05 | 30/45 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.8 | 7e-05 | 29/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.003 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.018 | 27/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.024 | 17/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.086 | 19/49 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.091 | 8/48 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.207×** | -34.3 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.212×** | -33.8 | 0e+00 | 48/48 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.287×** | -27.2 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.478×** | -16.1 | 0e+00 | 48/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.599×** | -11.2 | 5e-27 | 46/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.717×** | -10.3 | 7e-23 | 42/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -9.0 | 3e-17 | 42/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -8.9 | 5e-17 | 38/48 (A498, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -7.9 | 2e-13 | 47/49 (J82, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.784×** | -5.3 | 6e-06 | 29/49 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.803×** | -4.8 | 8e-05 | 27/48 (SW 1271, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **0.801×** | -4.7 | 1e-04 | 24/44 (SNU-1, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.865× | -4.5 | 3e-04 | 23/48 (LOX-IMVI, A-172, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.816×** | -4.5 | 3e-04 | 25/48 (C32, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.679×** | -4.4 | 4e-04 | 29/49 (LOX-IMVI, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -4.4 | 4e-04 | 19/48 (A-172, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.819×** | -4.4 | 4e-04 | 28/49 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 0.841× | -3.8 | 0.004 | 20/48 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.864× | -3.2 | 0.033 | 12/48 (SNU-423, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 162 | 8 (3 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.218× (z -24.2) |
| [[A-172 (line)]] | wt | 185 | 1 | 12 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.88× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.154× (z -27.2) |
| [[SW480 (line)]] | alt | 153 | 8 (2 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.173× (z -31.8) |
| [[LOX-IMVI (line)]] | wt | 227 | 2 | 8 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 280 | 7 (2 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.201× (z -23.2) |
| [[A498 (line)]] | wt | 346 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -28.6) |
| [[A549 (line)]] | wt | 305 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -30.8) |
| [[AsPC-1 (line)]] | alt | 115 | 5 (2 ⚠) | 4 | [[Bortezomib (drug)]] 0.05 µM 2.91× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.204× (z -22.5) |
| [[C32 (line)]] | wt | 163 | 3 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -20.1) |
| [[HOP62 (line)]] | alt | 196 | 3 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.170× (z -25.7) |
| [[Hs 766T (line)]] | wt | 257 | 4 (1 ⚠) | 5 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -27.2) |
| [[HS-578T (line)]] | alt | 216 | 1 | 8 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.140× (z -26.2) |
| [[HT-29 (line)]] | alt | 127 | 4 (1 ⚠) | 5 | [[Ixazomib citrate (drug)]] 5 µM 3.64× (z +17.8) | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -20.0) |
| [[J82 (line)]] | alt | 324 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -32.2) |
| [[LoVo (line)]] | wt | 167 | 5 (1 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 2.61× (z +14.6) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.56× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -22.9) |
| [[LS 180 (line)]] | wt | 195 | 4 | 5 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -22.3) |
| [[RKO (line)]] | wt | 368 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -24.2) |
| [[SNU-1 (line)]] | wt | 312 | 2 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -24.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.203× (z -20.3) |
| [[SW1417 (line)]] | alt | 194 | 3 | 6 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.18× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -21.2) |
| [[H4 (line)]] | wt | 221 | 3 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.165× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 168 | 3 (1 ⚠) | 5 | [[Niclosamide (olamine) (drug)]] 5 µM 2.66× (z +9.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.178× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 172 | 4 (1 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.175× (z -20.7) |
| [[KATO III (line)]] | alt | 170 | 4 | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.174× (z -24.5) |
| [[MIA PaCa-2 (line)]] | alt | 319 | 3 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.105× (z -33.2) |
| [[SW48 (line)]] | wt | 241 | 2 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -20.3) |
| [[HCT15 (line)]] | alt | 183 | 4 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.299× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 133 | 2 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -24.5) |
| [[Panc 03.27 (line)]] | alt | 178 | 2 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.193× (z -22.4) |
| [[SHP-77 (line)]] | alt | 183 | 3 | 4 | [[Bortezomib (drug)]] 0.05 µM 2.46× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.207× (z -20.4) |
| [[SNU-423 (line)]] | alt | 249 | 3 | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -21.9) |
| [[CFPAC-1 (line)]] | alt | 92.8 | 3 | 3 | [[Bortezomib (drug)]] 0.05 µM 2.45× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -16.3) |
| [[COLO 205 (line)]] | alt | 122 | 4 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 5.32× (z +16.9) | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 229 | 2 | 4 | [[Bortezomib (drug)]] 0.05 µM 2.17× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.251× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 144 | 2 (1 ⚠) | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.15× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.193× (z -22.1) |
| [[RPMI-7951 (line)]] | alt | 165 | 3 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 212 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -22.9) |
| [[BT-474 (line)]] | alt | 178 | 1 | 4 | [[Bortezomib (drug)]] 0.05 µM 2.03× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -26.6) |
| [[C-33 A (line)]] | alt | 201 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 236 | 1 | 4 | [[Bortezomib (drug)]] 0.05 µM 2.01× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -22.2) |
| [[NCI-H2347 (line)]] | alt | 175 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -25.6) |
| [[A-427 (line)]] | wt | 126 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -22.1) |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -18.1) |
| [[SW 900 (line)]] | alt | 169 | 1 | 3 | [[Bortezomib (drug)]] 0.05 µM 2.10× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.193× (z -20.1) |
| [[AN3 CA (line)]] | alt | 219 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.211× (z -13.5) |
| [[SW 1271 (line)]] | alt | 226 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -13.1) |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -9.1) |
| [[SW 1088 (line)]] | alt | 159 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5A]] | +0.62 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MAP4]] | +0.61 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[UBE2Q2]] | +0.60 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[IDE]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[CLCC1]] | +0.57 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[NSMAF]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SELENOI]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[GLRX3]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.54 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[KCTD15]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ME2]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[POLR3E]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INIP]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[NME7]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[NFKBIE]] | -0.53 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[DBP]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MEIS1]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CCDC148]] | -0.52 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[WRAP53]] | -0.51 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[PPP1R3B]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[CTR9]] | -0.50 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[DAD1]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MAP3K13]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CFAP20]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.8, 16.5); signed map (-11.5, -38.1). **Vector** length 118, 45.8% of its response variance represented; |z| ≥ 3 in 1,606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.3 | +17.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.3 | +16.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +14.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | -1.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.8 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -13.2 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.5 | +0.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.4 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -11.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | Ecm29 proteasome adaptor and scaffold |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:111,360,685-111,484,745 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22036, ECM29; previously KIAA0368 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VYK3](https://www.uniprot.org/uniprotkb/Q5VYK3) (Proteasome adapter and scaffold protein ECM29):

> Adapter/scaffolding protein that binds to the 26S proteasome, motor proteins and other compartment specific proteins. May couple the proteasome to different compartments including endosome, endoplasmic reticulum and centrosome. May play a role in ERAD and other enhanced proteolysis. Promotes proteasome dissociation under oxidative stress (By similarity).

**Summary**, from NCBI Gene [23392](https://www.ncbi.nlm.nih.gov/gene/23392):

> Enables proteasome binding activity. Involved in ERAD pathway. Located in several cellular components, including centrosome; cytoplasmic vesicle; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29020) · Entrez [23392](https://www.ncbi.nlm.nih.gov/gene/23392) · UniProt [Q5VYK3](https://www.uniprot.org/uniprotkb/Q5VYK3) · Ensembl [ENSG00000136813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136813)

## Data

Gene col 5907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5907); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5907]; `tensor/DDL_lfc|DDL_z.npy` [5907]; `embed/gene_vectors.npy` [5907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5907 or target_col == 5907). Every well: [[ECPAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECPAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
