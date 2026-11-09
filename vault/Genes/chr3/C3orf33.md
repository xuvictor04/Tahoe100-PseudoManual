---
symbol: "C3orf33"
type: "gene"
col: 10543
ensembl_id: "ENSG00000174928"
name: "mitochondrial inner membrane subdomain organizer 1"
location: "3q25.31"
module: 175
arm: "+"
pooled_cpm: 10.91
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# C3orf33

*mitochondrial inner membrane subdomain organizer 1* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +7.5, q 5e-11, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.579× (z -8.0, q 5e-13, down in 25 of 45 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Allantoin (drug)]] 5 µM: 0.796× (z -3.9, q 0.011, down in 10 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A14]] (+0.60, fdr 1e-04), [[FOXO3B]] (+0.59, fdr 1e-05), [[ZC3H8]] (+0.58, fdr 1e-05); moves opposite to [[USP9X]] (-0.55, fdr 3e-05), [[EIF4EBP2]] (-0.53, fdr 2e-04), [[TAGLN2]] (-0.51, fdr 2e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MVB12B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.5 | 5e-11 | 24/45 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.1 | 3e-07 | 20/39 (A-172, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.9 | 7e-07 | 19/45 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 2e-05 | 13/45 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.28×** | +4.6 | 5e-04 | 11/45 (Panc 03.27, A549, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.33×** | +4.0 | 0.007 | 14/43 (A498, NCI-H2347, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.8 | 0.013 | 12/45 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.070 | 4/40 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.23× | +3.1 | 0.13 | 10/44 (hTERT-HPNE, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.579×** | -8.0 | 5e-13 | 25/45 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.678×** | -5.7 | 3e-06 | 22/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.701×** | -5.2 | 3e-05 | 17/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.733×** | -4.6 | 6e-04 | 16/37 (HEC-1-A, A-427, …) | inconsistent across doses | composition shift |
| [[Allantoin (drug)]] 5 µM |  | **0.796×** | -3.9 | 0.011 | 10/45 (HCT15, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.775×** | -3.8 | 0.015 | 17/44 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.784×** | -3.6 | 0.027 | 7/46 (C-33 A, A549, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.046 | 9/45 (SW1417, A-427, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.064 | 9/45 (A-427, C-33 A, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.064 | 9/43 (LOX-IMVI, C32, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.813× | -3.1 | 0.11 | 16/44 (SW48, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 39.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW1417 (line)]] | alt | 7.01 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A498 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0941× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[LOX-IMVI (line)]] | wt | 8.04 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 7.41 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.149× (z -8.6) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0633× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[PANC-1 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0939× (z -16.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 6.11 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0728× (z -8.9) |
| [[SW48 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0894× (z -10.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | +0.60 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[FOXO3B]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZC3H8]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TMEM267]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TERB1]] | +0.57 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[DNAJC2]] | +0.57 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[ZNF343]] | +0.57 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[MTO1]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[WHAMMP2]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[ZNF25]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TXNDC15]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP9X]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[EIF4EBP2]] | -0.53 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[TAGLN2]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PPP1CA]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TGOLN2]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[POLR2E]] | -0.50 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[SRGAP2]] | -0.49 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[DIAPH1]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PRKCA]] | -0.48 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ATP7A]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[FRYL]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[FGFRL1]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises C3orf33's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without MVB12B | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[PRTG]] | B | PRTG activity raises C3orf33's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without PRTG | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[RRN3P1]] | B | RRN3P1 activity lowers C3orf33's level | lines that do not express RRN3P1 (9) vs lines expressing it (41) | 1.27× higher at baseline in the lines without RRN3P1 | 0.080 | ⚠ within organs, on part of the lines; co-absent genes |
| [[PSMB5]] | B | PSMB5 activity lowers C3orf33's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, 20.8); signed map (-15.7, -23.8). **Vector** length 77.0, 14.0% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.6 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.9 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.1 | -8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.3 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -4.1 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.5 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial inner membrane subdomain organizer 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:155,762,617-155,806,278 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MISO, FLJ31139, AC3-33; previously C3orf33 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1S2](https://www.uniprot.org/uniprotkb/Q6P1S2) (Mitochondrial inner membrane subdomain organizer 1):

> Regulates mitochondrial morphology and mitochondrial DNA (mtDNA) homeostasis. Promotes the formation of specialized mitochondrial subdomains called small MTFP1-enriched mitochondria (SMEM). Negatively regulates mitochondrial fusion by excluding fusion coordinator OPA1 from SMEM. Recruits mtDNA, potentially through interaction with SSBP1, and facilitates mtDNA transport to the mitochondrial periphery. Also recruits other proteins, including PHB1, PHB2 and MTFP1, into SMEM which promotes …

**Summary**, from NCBI Gene [285315](https://www.ncbi.nlm.nih.gov/gene/285315):

> Involved in negative regulation of ERK1 and ERK2 cascade. Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26434) · Entrez [285315](https://www.ncbi.nlm.nih.gov/gene/285315) · UniProt [Q6P1S2](https://www.uniprot.org/uniprotkb/Q6P1S2) · Ensembl [ENSG00000174928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174928)

## Data

Gene col 10543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10543); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10543]; `tensor/DDL_lfc|DDL_z.npy` [10543]; `embed/gene_vectors.npy` [10543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10543 or target_col == 10543). Every well: [[C3orf33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
