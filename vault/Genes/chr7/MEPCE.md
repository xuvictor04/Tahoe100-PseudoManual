---
symbol: "MEPCE"
type: "gene"
col: 7125
ensembl_id: "ENSG00000146834"
name: "methylphosphate capping enzyme"
location: "7q22.1"
module: 173
arm: "+"
pooled_cpm: 18.3
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# MEPCE

*methylphosphate capping enzyme* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +16.0, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.239× (z -17.1, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF1]] (+0.80, fdr 7e-06), [[FIZ1]] (+0.78, fdr 1e-05), [[BRPF3]] (+0.77, fdr 1e-05); moves opposite to [[SLC9A6]] (-0.68, fdr 4e-05), [[SDHB]] (-0.66, fdr 1e-05), [[HDAC3]] (-0.66, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABCA10]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +16.0 | 0e+00 | 38/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +8.8 | 4e-16 | 39/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +7.7 | 3e-12 | 33/47 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.6 | 4e-06 | 5/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 4e-04 | 25/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.5 | 6e-04 | 18/46 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +4.3 | 0.001 | 22/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.002 | 24/47 (KATO III, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.7 | 0.015 | 17/44 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.026 | 16/48 (Hs 766T, HOP62, …) | rises with dose | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.036 | 16/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.037 | 15/48 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.046 | 14/47 (HT-29, BT-474, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.099 | 11/47 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.239×** | -17.1 | 0e+00 | 46/47 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.280×** | -15.2 | 0e+00 | 47/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.320×** | -13.6 | 1e-39 | 45/48 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.392×** | -11.2 | 9e-27 | 45/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.479×** | -8.8 | 2e-16 | 38/45 (RPMI-7951, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.346×** | -6.6 | 4e-09 | 41/48 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -4.9 | 9e-05 | 26/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.751×** | -4.9 | 9e-05 | 26/48 (H4, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -4.3 | 1e-03 | 18/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.789×** | -4.0 | 0.003 | 26/48 (SW 1271, SW 900, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -3.9 | 0.005 | 17/47 (A-172, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -3.7 | 0.010 | 21/48 (SK-MEL-2, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.042 | 19/48 (A498, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.763×** | -3.2 | 0.049 | 18/46 (NCI-H2030, NCI-H23, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 21.1 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.163× (z -10.3) |
| [[HOP62 (line)]] | alt | 13.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.4) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.168× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0809× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.149× (z -13.1) |
| [[PANC-1 (line)]] | alt | 21.0 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.230× (z -12.0) |
| [[A498 (line)]] | wt | 22.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +14.8) | [[Belinostat (drug)]] 5 µM 0.310× (z -8.9) |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.237× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.216× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 15.1 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +16.6) | [[Belinostat (drug)]] 5 µM 0.194× (z -11.8) |
| [[C32 (line)]] | wt | 39.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +12.8) | [[Belinostat (drug)]] 5 µM 0.170× (z -9.6) |
| [[LoVo (line)]] | wt | 22.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.234× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 16.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.121× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.124× (z -10.9) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.191× (z -9.2) |
| [[A-427 (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.177× (z -10.7) |
| [[HS-578T (line)]] | alt | 11.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.0903× (z -12.2) |
| [[KATO III (line)]] | alt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.193× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0901× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.108× (z -9.9) |
| [[SW48 (line)]] | wt | 18.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0879× (z -9.6) |
| [[SW480 (line)]] | alt | 24.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.268× (z -10.6) |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -10.1) |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.133× (z -9.4) |
| [[J82 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 25.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.213× (z -9.2) |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.5) |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0851× (z -12.7) |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.211× (z -10.4) |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF1]] | +0.80 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.78 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[BRPF3]] | +0.77 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.74 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[USP11]] | +0.73 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[PIGV]] | +0.73 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.72 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[AKT1S1]] | +0.72 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[SIX5]] | +0.71 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.71 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[FKRP]] | +0.71 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[PCBP1-AS1]] | +0.71 | +0.75 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.68 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[SDHB]] | -0.66 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.66 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.66 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[ANKRD27]] | -0.65 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[PLA2G12A]] | -0.65 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[SBF2]] | -0.65 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[HEBP1]] | -0.64 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[SEC11A]] | -0.64 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.64 | -0.55 / -0.25 | both halves | 4e-04 |  |
| [[STX7]] | -0.64 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[PCMT1]] | -0.64 | -0.63 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA10]] | B | ABCA10 activity raises MEPCE's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without ABCA10 | 0.038 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | MEPCE's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | MEPCE's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.432 over the table, 0.045 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.852). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.2, 5.7); signed map (15.4, -21.9). **Vector** length 121, 32.4% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.7 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.6 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.7 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.8 | -17.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.9 | -11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.9 | -15.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -13.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.1 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | methylphosphate capping enzyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,428,322-100,434,126 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20257; previously BCDIN3 |
| Gene groups (HGNC) | 7SK snRNP complex; 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L2J0](https://www.uniprot.org/uniprotkb/Q7L2J0) (7SK snRNA methylphosphate capping enzyme):

> S-adenosyl-L-methionine-dependent methyltransferase that adds a methylphosphate cap at the 5'-end of 7SK snRNA (7SK RNA), leading to stabilize it. Also has a non-enzymatic function as part of the 7SK RNP complex: the 7SK RNP complex sequesters the positive transcription elongation factor b (P-TEFb) in a large inactive 7SK RNP complex preventing RNA polymerase II phosphorylation and subsequent transcriptional elongation. The 7SK RNP complex also promotes snRNA gene transcription by RNA …

**Summary**, from NCBI Gene [56257](https://www.ncbi.nlm.nih.gov/gene/56257):

> Enables 7SK snRNA binding activity and RNA 5'-gamma-phosphate methyltransferase activity. Involved in RNA modification; positive regulation of protein localization to Cajal body; and positive regulation of snRNA transcription by RNA polymerase II. Located in nucleus. Part of 7SK snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20247) · Entrez [56257](https://www.ncbi.nlm.nih.gov/gene/56257) · UniProt [Q7L2J0](https://www.uniprot.org/uniprotkb/Q7L2J0) · Ensembl [ENSG00000146834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146834)

## Data

Gene col 7125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7125); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7125]; `tensor/DDL_lfc|DDL_z.npy` [7125]; `embed/gene_vectors.npy` [7125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7125 or target_col == 7125). Every well: [[MEPCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEPCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
