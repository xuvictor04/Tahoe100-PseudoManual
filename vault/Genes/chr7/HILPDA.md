---
symbol: "HILPDA"
type: "gene"
col: 5668
ensembl_id: "ENSG00000135245"
name: "hypoxia inducible lipid droplet associated"
location: "7q32.1"
module: 79
arm: "+"
pooled_cpm: 137.53
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 30
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# HILPDA

*hypoxia inducible lipid droplet associated* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.70× (z +5.7, q 8e-06, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.0953× (z -24.8, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM162A]] (+0.86, fdr 7e-06), [[PDK3]] (+0.81, fdr 7e-06), [[ANKRD37]] (+0.81, fdr 7e-06); moves opposite to [[MAPKAPK5]] (-0.68, fdr 7e-06), [[PARVA]] (-0.66, fdr 1e-05), [[AVEN]] (-0.64, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +5.7 | 8e-06 | 44/47 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +5.1 | 1e-04 | 34/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +4.9 | 2e-04 | 37/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +4.6 | 5e-04 | 43/48 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.008 | 37/48 (HT-29, PANC-1, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.009 | 42/47 (COLO 205, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fumaric acid (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.080 | 34/48 (A-172, AsPC-1, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.0953×** | -24.8 | 0e+00 | 47/47 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.273×** | -13.7 | 4e-40 | 47/48 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.195×** | -12.2 | 5e-32 | 46/47 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.218×** | -10.9 | 1e-25 | 42/42 (CHP-212, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.252×** | -9.9 | 5e-21 | 42/47 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.417×** | -9.2 | 4e-18 | 46/47 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.267×** | -8.6 | 9e-16 | 44/47 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.321×** | -8.2 | 3e-14 | 42/46 (C32, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.489×** | -7.5 | 4e-12 | 42/47 (C32, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.339×** | -7.4 | 6e-12 | 40/43 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.422×** | -6.2 | 4e-08 | 44/47 (hTERT-HPNE, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.527×** | -4.6 | 2e-04 | 33/46 (SW 1271, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.522×** | -4.6 | 2e-04 | 36/46 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.318×** | -4.5 | 3e-04 | 39/48 (NCI-H2347, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -4.3 | 6e-04 | 35/49 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.567×** | -4.2 | 9e-04 | 30/47 (hTERT-HPNE, SW 1271, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.598×** | -3.8 | 0.004 | 33/47 (SW48, hTERT-HPNE, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.587×** | -3.8 | 0.004 | 35/47 (NCI-H2347, C-33 A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.380×** | -3.8 | 0.004 | 30/48 (MIA PaCa-2, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.613×** | -3.6 | 0.007 | 33/47 (H4, SW 1271, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 591 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0148× (z -41.8) |
| [[NCI-H460 (line)]] | wt | 169 | 7 (4 ⚠) | 5 | [[Digitoxin (drug)]] 5 µM 9.75× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 7.91× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -24.7) |
| [[A-172 (line)]] | wt | 160 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0778× (z -21.9) |
| [[hTERT-HPNE (line)]] | wt | 320 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0260× (z -32.3) |
| [[NCI-H2347 (line)]] | alt | 195 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -28.3) |
| [[A549 (line)]] | wt | 189 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0475× (z -28.4) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0324× (z -25.9) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 2 (1 ⚠) | 6 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +10.0) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.21× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -23.0) |
| [[NCI-H1573 (line)]] | alt | 200 | 2 (1 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 5.55× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.99× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.0399× (z -24.8) |
| [[SW 900 (line)]] | alt | 344 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0503× (z -24.5) |
| [[C-33 A (line)]] | alt | 242 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0550× (z -27.4) |
| [[CHP-212 (line)]] | wt | 316 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0363× (z -28.2) |
| [[HOP62 (line)]] | alt | 225 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -24.8) |
| [[HS-578T (line)]] | alt | 273 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0343× (z -27.2) |
| [[NCI-H1792 (line)]] | alt | 175 | 2 (1 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 6.23× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.0370× (z -27.7) |
| [[SNU-423 (line)]] | alt | 194 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0323× (z -28.1) |
| [[SW 1271 (line)]] | alt | 401 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0242× (z -23.6) |
| [[SW48 (line)]] | wt | 311 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0181× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 284 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0723× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -19.8) |
| [[PANC-1 (line)]] | alt | 91.0 | 2 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.06× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.0817× (z -23.0) |
| [[RPMI-7951 (line)]] | alt | 182 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -27.8) |
| [[H4 (line)]] | wt | 454 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0110× (z -34.2) |
| [[BT-474 (line)]] | alt | 118 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -19.3) |
| [[HCT15 (line)]] | alt | 144 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0448× (z -24.1) |
| [[Hs 766T (line)]] | wt | 82.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -19.6) |
| [[J82 (line)]] | alt | 135 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.41× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.7) |
| [[SNU-1 (line)]] | wt | 124 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -14.7) |
| [[AN3 CA (line)]] | alt | 100 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -18.6) |
| [[SW480 (line)]] | alt | 37.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 42.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -11.0) |
| [[COLO 205 (line)]] | alt | 64.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0638× (z -21.9) |
| [[LoVo (line)]] | wt | 48.2 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.17× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -14.1) |
| [[SHP-77 (line)]] | alt | 64.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -15.7) |
| [[SW 1088 (line)]] | alt | 339 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -13.2) |
| [[A498 (line)]] | wt | 58.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 60.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -16.6) |
| [[HT-29 (line)]] | alt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.1) |
| [[KATO III (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.0) |
| [[LS 180 (line)]] | wt | 73.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 71.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.0) |
| [[NCI-H661 (line)]] | alt | 45.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 60.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -12.4) |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.3) |
| [[A-427 (line)]] | wt | 27.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM162A]] | +0.86 | +0.87 / +0.78 | both halves | 7e-06 |  |
| [[PDK3]] | +0.81 | +0.88 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.81 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.78 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[ENO2]] | +0.76 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.75 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.74 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[FUT11]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[RFX2]] | +0.73 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ABCB9]] | +0.72 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.68 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[PARVA]] | -0.66 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[AVEN]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.63 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[VPS52]] | -0.63 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.63 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[U2AF2]] | -0.61 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[TASOR]] | -0.61 | -0.69 / -0.39 | both halves | 6e-05 |  |
| [[MCM3AP]] | -0.61 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[UTP20]] | -0.61 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises HILPDA's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.10× lower at baseline in the lines without PLOD2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[PPP1R3C]] | B | PPP1R3C activity raises HILPDA's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without PPP1R3C | 0.043 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[TOP2A]] | B | TOP2A activity raises HILPDA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MLLT3]] | B | MLLT3 activity raises HILPDA's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without MLLT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.889). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -15.5); signed map (-34.9, 23.5). **Vector** length 161, 64.4% of its response variance represented; |z| ≥ 3 in 1,464 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.64 to 16); *hypoxia* (control, mean cos +0.70 to 5); *glycolysis* (hallmark, mean cos +0.68 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.6 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +10.7 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.3 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +10.1 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +10.1 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.4 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.2 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Silodosin (drug)]] 5 µM |  | +3.7 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -24.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.5 | -10.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -12.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.8 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.5 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | hypoxia inducible lipid droplet associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,455,849-128,458,418 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21076, HIG-2, HIG2; previously C7orf68 |
| Reactome | 1 pathways, smallest: Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5L2](https://www.uniprot.org/uniprotkb/Q9Y5L2) (Hypoxia-inducible lipid droplet-associated protein):

> Increases intracellular lipid accumulation. Stimulates expression of cytokines including IL6, MIF and VEGFA. Enhances cell growth and proliferation.

**Summary**, from NCBI Gene [29923](https://www.ncbi.nlm.nih.gov/gene/29923):

> Enables signaling receptor binding activity. Involved in several processes, including autocrine signaling; cellular response to hypoxia; and positive regulation of lipid storage. Located in several cellular components, including lipid droplet; obsolete extracellular space; and secretory granule. Implicated in colorectal cancer and hepatocellular carcinoma. Biomarker of colorectal cancer and hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28859) · Entrez [29923](https://www.ncbi.nlm.nih.gov/gene/29923) · UniProt [Q9Y5L2](https://www.uniprot.org/uniprotkb/Q9Y5L2) · Ensembl [ENSG00000135245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135245)

## Data

Gene col 5668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5668); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5668]; `tensor/DDL_lfc|DDL_z.npy` [5668]; `embed/gene_vectors.npy` [5668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5668 or target_col == 5668). Every well: [[HILPDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HILPDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
