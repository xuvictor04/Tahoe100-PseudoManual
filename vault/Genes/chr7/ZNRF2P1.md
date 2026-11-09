---
symbol: "ZNRF2P1"
type: "gene"
col: 14111
ensembl_id: "ENSG00000237004"
name: "zinc and ring finger 2 pseudogene 1"
location: "7p14.3"
module: 18
arm: "+"
pooled_cpm: 25.77
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ZNRF2P1

*zinc and ring finger 2 pseudogene 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.81× (z +10.1, q 4e-21, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.406× (z -15.2, q 0e+00, down in 33 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.531× (z -5.6, q 2e-06, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNRF2P2]] (+0.83, fdr 7e-06), [[DPY19L2P3]] (+0.57, fdr 3e-05), [[C2orf69]] (+0.57, fdr 3e-05); moves opposite to [[AP3D1]] (-0.55, fdr 2e-05), [[DYNC1LI2]] (-0.53, fdr 3e-05), [[SPTLC1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +10.1 | 4e-21 | 32/48 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 1e-13 | 28/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +8.0 | 3e-13 | 29/47 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.7 | 3e-12 | 29/46 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 4e-04 | 19/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.20× | +4.4 | 0.001 | 19/48 (J82, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.028 | 8/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.21× | +3.2 | 0.11 | 12/47 (A498, HepG2/C3A, …) | top dose only | position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.14 | 1/47 (SNU-1) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.13× | +3.0 | 0.14 | 5/48 (CFPAC-1, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.406×** | -15.2 | 0e+00 | 33/41 (SW1417, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.497×** | -11.8 | 2e-29 | 38/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -11.5 | 3e-28 | 31/38 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.545×** | -9.8 | 1e-20 | 25/35 (C32, SHP-77, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.609×** | -8.3 | 8e-15 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.716×** | -5.6 | 2e-06 | 22/48 (NCI-H460, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.531×** | -5.6 | 2e-06 | 23/48 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.818×** | -4.7 | 1e-04 | 24/47 (NCI-H23, C32, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -4.7 | 2e-04 | 19/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.4 | 6e-04 | 3/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.771×** | -4.4 | 7e-04 | 20/44 (HCT15, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.622×** | -4.2 | 0.001 | 16/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.807×** | -3.6 | 0.015 | 13/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.678×** | -3.4 | 0.026 | 10/46 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.3 | 0.036 | 14/48 (A-427, NCI-H460, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.689×** | -3.3 | 0.039 | 10/45 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.769×** | -3.0 | 0.093 | 12/46 (SW 900, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.1 | 1 | 9 (9 ⚠) | [[Digitoxin (drug)]] 0.05 µM 2.79× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.170× (z -17.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 30.1 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 54.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 40.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 24.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 20.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 44.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 28.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~88% of this change |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0711× (z -14.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0986× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0889× (z -16.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0861× (z -9.4) |
| [[C-33 A (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.162× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.107× (z -9.1) ⚠ toxic |
| [[KATO III (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0479× (z -10.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 9.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0951× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -9.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2P2]] | +0.83 | +0.85 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[DPY19L2P3]] | +0.57 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[C2orf69]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[BRWD1]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[DPY19L1P1]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[KIF9-AS1]] | +0.53 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[PKD2]] | +0.53 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[ACVR1B]] | +0.53 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[ARHGEF11]] | +0.52 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[ZNRF2]] | +0.51 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CRTC3]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[HOXB6]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PTGR3]] | +0.50 | +0.52 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3D1]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[DYNC1LI2]] | -0.53 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SPTLC1]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[MSANTD1]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[HAPSTR1]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[AP1G1]] | -0.51 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[ASCC2]] | -0.50 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[RTF2]] | -0.49 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[MKNK1]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GOLGA3]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ANXA2]] | -0.48 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[IRAG1-AS1]] | -0.48 | -0.63 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity lowers ZNRF2P1's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.56× higher at baseline in the lines without F3 | 0.005 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[F3]] | B | F3 activity weakens ZNRF2P1's drug response | lines that do not express F3 (24) vs lines expressing it (24) | the lines without F3 respond 1.24× as strongly (z diff -1.00); strongest at Dinaciclib 0.5 µM: 0.29x vs 0.51x (z diff -4.3) | 0.074 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.355). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.5, -53.3); signed map (6.8, -4.1). **Vector** length 88.3, 18.4% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +10.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.6 | +8.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +2.9 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.0 | +2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.0 | -15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.8 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.7 | -11.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.6 | -11.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc and ring finger 2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7p14.3 — chr7:32,728,569-32,729,011 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42792) · Entrez [441208](https://www.ncbi.nlm.nih.gov/gene/441208) · Ensembl [ENSG00000237004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237004)

## Data

Gene col 14111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14111); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14111]; `tensor/DDL_lfc|DDL_z.npy` [14111]; `embed/gene_vectors.npy` [14111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14111 or target_col == 14111). Every well: [[ZNRF2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNRF2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
