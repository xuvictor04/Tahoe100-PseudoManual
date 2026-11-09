---
symbol: "IFI27L1"
type: "gene"
col: 9214
ensembl_id: "ENSG00000165948"
name: "interferon alpha inducible protein 27 like 1"
location: "14q32.12"
module: 40
arm: "+"
pooled_cpm: 14.19
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IFI27L1

*interferon alpha inducible protein 27 like 1* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +19.5, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.568× (z -13.5, q 2e-38, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.459× (z -13.4, q 2e-38, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHRS1]] (+0.74, fdr 7e-06), [[IER3IP1]] (+0.74, fdr 7e-06), [[SEC11A]] (+0.70, fdr 7e-06); moves opposite to [[ZMYM4]] (-0.68, fdr 7e-06), [[RPL7L1]] (-0.65, fdr 7e-06), [[TMEM185B]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MICE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +19.5 | 0e+00 | 42/45 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +10.9 | 2e-25 | 39/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +10.9 | 3e-25 | 39/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +10.3 | 1e-22 | 41/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.47×** | +6.4 | 2e-08 | 22/46 (HOP62, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +5.7 | 1e-06 | 20/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.31×** | +4.6 | 3e-04 | 11/36 (SNU-423, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.5 | 4e-04 | 8/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.002 | 9/45 (SHP-77, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +4.1 | 0.002 | 15/45 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 12/48 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.009 | 10/48 (J82, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.017 | 6/42 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.025 | 11/45 (HT-29, SNU-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.055 | 4/47 (NCI-H2347, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.568×** | -13.5 | 2e-38 | 36/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.459×** | -13.4 | 2e-38 | 37/45 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.519×** | -10.8 | 4e-25 | 35/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -9.2 | 4e-18 | 27/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -8.9 | 8e-17 | 23/46 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -7.5 | 6e-12 | 20/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -7.4 | 1e-11 | 26/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -7.0 | 1e-10 | 21/38 (NCI-H1792, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -6.1 | 6e-08 | 23/48 (NCI-H460, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -5.4 | 3e-06 | 20/43 (H4, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.784×** | -4.0 | 0.004 | 16/47 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.9 | 0.004 | 14/44 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.802×** | -3.8 | 0.006 | 15/47 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.027 | 6/48 (MIA PaCa-2, AsPC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.3 | 0.031 | 18/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.031 | 13/47 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.031 | 15/47 (A-172, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.201× (z -12.4) |
| [[A549 (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.217× (z -8.6) |
| [[HOP62 (line)]] | alt | 11.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.203× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0599× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[9-ING-41 (drug)]] 0.5 µM 0.0655× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 18.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 9.78 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -8.7) |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 2 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.181× (z -9.5) |
| [[SNU-423 (line)]] | alt | 17.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.0) | [[Cobimetinib (drug)]] 5 µM 0.152× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0953× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.7) | — |
| [[SW480 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.2) | — |
| [[A-172 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS1]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GPR107]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.67 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[HSPB11]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SNHG30]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TMEM50B]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RARS2]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[SDHAP4]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | -0.68 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[RPL7L1]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.64 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[LYRM2]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[COMMD10]] | -0.63 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TIAM2]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[COA7]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[PUF60]] | -0.61 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[ZNF518B]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TASOR]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[THADA]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ZNF474]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICE]] | B | MICE activity raises IFI27L1's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without MICE | 0.083 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers IFI27L1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-3.4, -14.8); signed map (-43.5, 5.5). **Vector** length 82.2, 15.7% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +19.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.9 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.3 | +5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +2.0 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | +1.4 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.0 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | interferon alpha inducible protein 27 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:94,081,301-94,103,846 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM14B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BM0](https://www.uniprot.org/uniprotkb/Q96BM0) (Interferon alpha-inducible protein 27-like protein 1):

> Plays a role in the apoptotic process and has a pro-apoptotic activity.

**Summary**, from NCBI Gene [122509](https://www.ncbi.nlm.nih.gov/gene/122509):

> Predicted to enable molecular adaptor activity. Involved in apoptotic process. Predicted to be located in membrane. Predicted to be active in mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19754) · Entrez [122509](https://www.ncbi.nlm.nih.gov/gene/122509) · UniProt [Q96BM0](https://www.uniprot.org/uniprotkb/Q96BM0) · Ensembl [ENSG00000165948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165948)

## Data

Gene col 9214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9214); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9214]; `tensor/DDL_lfc|DDL_z.npy` [9214]; `embed/gene_vectors.npy` [9214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9214 or target_col == 9214). Every well: [[IFI27L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI27L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
