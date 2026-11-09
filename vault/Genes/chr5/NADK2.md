---
symbol: "NADK2"
type: "gene"
col: 7646
ensembl_id: "ENSG00000152620"
name: "NAD kinase 2, mitochondrial"
location: "5p13.2"
module: 94
arm: "+"
pooled_cpm: 38.19
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# NADK2

*NAD kinase 2, mitochondrial* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.55× (z +10.5, q 7e-23, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +8.6, q 3e-15, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.391× (z -16.0, q 0e+00, down in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.768× (z -4.5, q 3e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A14]] (+0.67, fdr 1e-05), [[ZNF25]] (+0.61, fdr 1e-05), [[CCT6P1]] (+0.60, fdr 2e-04); moves opposite to [[GALNS]] (-0.52, fdr 2e-04), [[KANK2]] (-0.51, fdr 3e-04), [[PI4KA]] (-0.51, fdr 2e-04).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ACP6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.55×** | +10.5 | 7e-23 | 41/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.6 | 3e-15 | 31/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.46×** | +6.4 | 3e-08 | 35/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 5e-07 | 30/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +5.0 | 5e-05 | 31/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.011 | 12/48 (NCI-H2347, A-427, …) | inconsistent across doses | position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.025 | 12/48 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.055 | 13/48 (LS 180, BT-474, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.090 | 12/48 (HOP62, SW 1088, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.10 | 10/48 (LoVo, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.391×** | -16.0 | 0e+00 | 45/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.414×** | -15.0 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.428×** | -14.4 | 7e-45 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.457×** | -13.3 | 3e-38 | 43/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.534×** | -10.7 | 2e-24 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.540×** | -10.5 | 1e-23 | 37/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.540×** | -10.5 | 1e-23 | 40/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -6.0 | 2e-07 | 28/44 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.525×** | -5.7 | 6e-07 | 29/48 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.739×** | -5.1 | 2e-05 | 32/48 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.756×** | -4.8 | 1e-04 | 28/48 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.826×** | -4.6 | 2e-04 | 21/48 (MIA PaCa-2, SNU-1, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -4.5 | 3e-04 | 24/48 (C32, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -4.3 | 6e-04 | 21/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.616×** | -4.3 | 6e-04 | 17/48 (H4, A498, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -4.2 | 1e-03 | 19/48 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.843× | -4.1 | 0.001 | 20/48 (Panc 03.27, SW 1271, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.003 | 22/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -3.9 | 0.003 | 17/48 (A-427, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -3.8 | 0.003 | 19/48 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.701×** | -3.2 | 0.036 | 11/48 (LOX-IMVI, A498, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.713×** | -3.0 | 0.057 | 14/47 (HepG2/C3A, A498, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.830×** | -3.0 | 0.059 | 14/47 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.6 | 0 | 11 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 78.7 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 32.7 | 1 | 7 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.159× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.0713× (z -12.1) |
| [[SW 900 (line)]] | alt | 52.4 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -16.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.1 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 58.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -13.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 79.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 61.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.250× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -10.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 32.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 30.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0757× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[LOX-IMVI (line)]] | wt | 27.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.55× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | [[Digitoxin (drug)]] 5 µM 0.243× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.04× (z +10.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Digitoxin (drug)]] 5 µM 0.148× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 49.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 42.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -10.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0623× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.335× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 47.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.353× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 40.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 69.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.444× (z -12.3) |
| [[KATO III (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.563× (z -15.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 38.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.7) | — |
| [[A-172 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | +0.67 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZNF25]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CCT6P1]] | +0.60 | +0.67 / +0.32 | both halves | 2e-04 |  |
| [[ALG5]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZNF419]] | +0.59 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[ZNF343]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TP53]] | +0.57 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[MCCC2]] | +0.57 | +0.54 / +0.42 | both halves | 4e-05 | pathway: Metabolism of vitamins and cofactors |
| [[ZNF563]] | +0.57 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[HOXC6]] | +0.56 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ANGEL2]] | +0.56 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[ZNF391]] | +0.56 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNS]] | -0.52 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[KANK2]] | -0.51 | -0.51 / -0.26 | both halves | 3e-04 |  |
| [[PI4KA]] | -0.51 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[SCART1]] | -0.51 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[AREG]] | -0.50 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[LMTK3]] | -0.50 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[PPCDC]] | -0.50 | -0.38 / -0.46 | both halves | 7e-05 | pathway: Metabolism of vitamins and cofactors |
| [[CHMP1A]] | -0.50 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[CYBA]] | -0.49 | -0.59 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[CADM4]] | -0.49 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[YWHAB]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[RALGAPA2]] | -0.47 | -0.43 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACP6]] | C | ACP6 activity weakens NADK2's drug response | lines that do not express ACP6 (3) vs lines expressing it (45) | the lines without ACP6 respond 1.37× as strongly (z diff -1.61); strongest at Digitoxin 0.5 µM: 0.29x vs 0.56x (z diff -4.7) | 0.061 | ⚠ few lines (3 vs 47); across organs; also absent: DBNDD1, CDKL5, ERO1B; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, 19.0); signed map (-31.2, -21.7). **Vector** length 107, 29.0% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +11.0 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +8.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +6.6 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +0.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.7 | -13.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.5 | -14.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.0 | -15.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NAD kinase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:36,192,589-36,242,279 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30596, MNADK; previously C5orf33, NADKD1 |
| Gene groups (HGNC) | NAD kinases |
| Reactome | 4 pathways, smallest: Nicotinate metabolism; Mitochondrial protein degradation; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0N4](https://www.uniprot.org/uniprotkb/Q4G0N4) (NAD kinase 2, mitochondrial):

> Mitochondrial NAD(+) kinase that phosphorylates NAD(+) to yield NADP(+). Can use both ATP or inorganic polyphosphate as the phosphoryl donor. Also has weak NADH kinase activity in vitro; however NADH kinase activity is much weaker than the NAD(+) kinase activity and may not be relevant in vivo.

**Summary**, from NCBI Gene [133686](https://www.ncbi.nlm.nih.gov/gene/133686):

> This gene encodes a mitochondrial kinase that catalyzes the phosphorylation of NAD to yield NADP. Mutations in this gene result in 2,4-dienoyl-CoA reductase deficiency. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:26404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26404) · Entrez [133686](https://www.ncbi.nlm.nih.gov/gene/133686) · UniProt [Q4G0N4](https://www.uniprot.org/uniprotkb/Q4G0N4) · Ensembl [ENSG00000152620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152620)

## Data

Gene col 7646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7646); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7646]; `tensor/DDL_lfc|DDL_z.npy` [7646]; `embed/gene_vectors.npy` [7646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7646 or target_col == 7646). Every well: [[NADK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NADK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
