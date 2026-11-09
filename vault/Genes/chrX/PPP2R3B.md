---
symbol: "PPP2R3B"
type: "gene"
col: 9462
ensembl_id: "ENSG00000167393"
name: "protein phosphatase 2 regulatory subunit B''beta"
location: "Xp22.3 and Yp11.3"
module: 67
arm: "+"
pooled_cpm: 10.57
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# PPP2R3B

*protein phosphatase 2 regulatory subunit B''beta* — Xp22.3 and Yp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.63× (z +5.3, q 6e-05, up in 15 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.547× (z -12.2, q 1e-31, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHTF18]] (+0.62, fdr 1e-05), [[E4F1]] (+0.61, fdr 1e-05), [[DTYMK]] (+0.61, fdr 1e-05); moves opposite to [[ARMT1]] (-0.53, fdr 3e-05), [[SMIM15]] (-0.53, fdr 5e-05), [[NXT2]] (-0.52, fdr 4e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRPS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +5.3 | 6e-05 | 15/40 (LoVo, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.2 | 0.008 | 11/33 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.014 | 11/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.016 | 13/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.035 | 13/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.035 | 6/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.091 | 3/46 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.547×** | -12.2 | 1e-31 | 35/45 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.479×** | -10.8 | 1e-24 | 32/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -10.6 | 4e-24 | 28/44 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.552×** | -9.0 | 3e-17 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.571×** | -8.5 | 2e-15 | 29/47 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -8.4 | 4e-15 | 26/44 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -8.3 | 6e-15 | 27/46 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.586×** | -8.1 | 4e-14 | 24/46 (NCI-H2030, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -7.1 | 6e-11 | 25/47 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -6.3 | 1e-08 | 22/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -6.2 | 3e-08 | 21/46 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.674×** | -5.6 | 8e-07 | 16/46 (HT-29, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -5.6 | 1e-06 | 17/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.565×** | -4.5 | 2e-04 | 11/46 (MIA PaCa-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.731×** | -4.5 | 3e-04 | 16/47 (SW48, SW 1088, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -3.9 | 0.003 | 18/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.008 | 10/48 (Hs 766T, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.5) |
| [[C32 (line)]] | wt | 7.07 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0507× (z -11.4) |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -18.1) |
| [[HOP62 (line)]] | alt | 6.95 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.4× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 7.60 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0537× (z -15.9) ⚠ toxic; cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.5) |
| [[J82 (line)]] | alt | 17.4 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.146× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.212× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -18.0) |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 5.79 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0757× (z -8.5) |
| [[LoVo (line)]] | wt | 9.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 5.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0527× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.182× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0922× (z -12.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 6.87 | 0 | 1 | — | [[Erdafitinib (drug)]] 0.05 µM 0.0743× (z -9.1) |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.6) |
| [[SW480 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -13.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTF18]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[E4F1]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DTYMK]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[UHRF2]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[DHTKD1]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SFI1]] | +0.59 | +0.44 / +0.57 | both halves | 3e-05 | pathway: G2/M Transition |
| [[TRAIP]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[POC1A]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SMYD4]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CEP131]] | +0.57 | +0.43 / +0.48 | both halves | 3e-05 | pathway: G2/M Transition |
| [[PPOX]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMT1]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SMIM15]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[NXT2]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[UBQLN2]] | -0.51 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NCOA4]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[RBM24]] | -0.49 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[TSPAN31]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LYRM2]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[POLR2M]] | -0.48 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[RNF6]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[MR1]] | -0.47 | -0.40 / -0.29 | both halves | 3e-04 |  |
| [[LINC01340]] | -0.47 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPS1]] | B | TRPS1 activity lowers PPP2R3B's level | lines that do not express TRPS1 (14) vs lines expressing it (36) | 1.60× higher at baseline in the lines without TRPS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, FBXO32, PRDM1 |
| [[LINC02405]] | B | LINC02405 activity lowers PPP2R3B's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 1.45× higher at baseline in the lines without LINC02405 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-29.1, -49.0); signed map (-49.6, -16.2). **Vector** length 64.4, 9.87% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.50 to 4); *Nucleosome assembly* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B''beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.3 and Yp11.3 — chrX:333,933-386,955 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP2R3LY, PR48, PR70; previously PPP2R3L |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; Pseudoautosomal region 1; EF-hand domain containing |
| Reactome | 11 pathways, smallest: Inhibition of replication initiation of damaged DNA by RB1/E2F1; E2F mediated regulation of DNA replication; Cyclin A/B1/B2 associated events during G2/M transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5P8](https://www.uniprot.org/uniprotkb/Q9Y5P8) (Serine/threonine-protein phosphatase 2A regulatory subunit B'' subunit beta):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment.

**Summary**, from NCBI Gene [28227](https://www.ncbi.nlm.nih.gov/gene/28227):

> Protein phosphatase 2 (formerly named type 2A) is one of the four major Ser/Thr phosphatases and is implicated in the negative control of cell growth and division. Protein phosphatase 2 holoenzymes are heterotrimeric proteins composed of a structural subunit A, a catalytic subunit C, and a regulatory subunit B. The regulatory subunit is encoded by a diverse set of genes that have been grouped into the B/PR55, B'/PR61, and B''/PR72 families. These different regulatory subunits confer distinct …

**Accessions** — [HGNC:13417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13417) · Entrez [28227](https://www.ncbi.nlm.nih.gov/gene/28227) · UniProt [Q9Y5P8](https://www.uniprot.org/uniprotkb/Q9Y5P8) · Ensembl [ENSG00000167393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167393)

## Data

Gene col 9462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9462); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9462]; `tensor/DDL_lfc|DDL_z.npy` [9462]; `embed/gene_vectors.npy` [9462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9462 or target_col == 9462). Every well: [[PPP2R3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
