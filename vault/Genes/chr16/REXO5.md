---
symbol: "REXO5"
type: "gene"
col: 72
ensembl_id: "ENSG00000005189"
name: "RNA exonuclease 5"
location: "16p12.3"
module: 91
arm: "+"
pooled_cpm: 7.9
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# REXO5

*RNA exonuclease 5* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +18.9, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.551× (z -7.1, q 8e-10, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESPL1]] (+0.79, fdr 7e-06), [[ESCO2]] (+0.73, fdr 7e-06), [[GEN1]] (+0.72, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 72.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +18.9 | 0e+00 | 38/42 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +12.9 | 9e-36 | 35/43 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.45×** | +11.3 | 2e-27 | 23/29 (SW 900, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +10.8 | 5e-25 | 31/40 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +10.5 | 2e-23 | 33/46 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.09×** | +9.0 | 3e-17 | 6/11 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.78×** | +7.0 | 3e-10 | 21/42 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.75×** | +6.6 | 4e-09 | 10/21 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.7 | 6e-07 | 18/41 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 3e-04 | 18/47 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 4e-04 | 18/46 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 6e-04 | 10/47 (SW480, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.014 | 8/47 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.095 | 2/47 (SW480, NCI-H23) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.095 | 7/40 (SW1417, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 72.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.551×** | -7.1 | 8e-10 | 27/43 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -6.8 | 3e-09 | 26/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -6.4 | 3e-08 | 21/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -5.1 | 6e-05 | 19/42 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -4.6 | 4e-04 | 17/46 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.706×** | -4.4 | 1e-03 | 17/45 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -4.4 | 1e-03 | 14/44 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.713×** | -4.3 | 0.001 | 17/44 (HCT15, A498, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.801×** | -4.0 | 0.005 | 16/46 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.655×** | -3.8 | 0.008 | 12/47 (PANC-1, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.023 | 16/45 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.023 | 9/47 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.824×** | -3.5 | 0.023 | 15/47 (A-427, H4, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.761×** | -3.4 | 0.023 | 14/47 (SW 1271, PANC-1, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.825×** | -3.4 | 0.023 | 9/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.2 | 0.046 | 13/46 (PANC-1, KATO III, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.778×** | -3.1 | 0.076 | 7/47 (HT-29, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -3.0 | 0.086 | 16/44 (PANC-1, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.848× | -2.9 | 0.098 | 11/48 (SW48, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 72. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.2 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.217× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 2.93 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +8.8) | [[Tadalafil (drug)]] 5 µM 0.0763× (z -9.2) |
| [[SW480 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0673× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -11.3) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.131× (z -10.5) |
| [[A-427 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -8.5) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HEC-1-A (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0475× (z -16.2) ⚠ toxic |
| [[J82 (line)]] | alt | 7.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +10.5) | — |
| [[LoVo (line)]] | wt | 4.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 4.83 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0710× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 7.00 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0690× (z -10.3) |
| [[RKO (line)]] | wt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0587× (z -8.6) |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 72), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESPL1]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[ESCO2]] | +0.73 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[GEN1]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[C1orf112]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[KIF24]] | +0.71 | +0.61 / +0.83 | both halves | 7e-06 |  |
| [[PHF19]] | +0.71 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[HIRIP3]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SGO1]] | +0.69 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[CIP2A]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[KIF11]] | +0.67 | +0.64 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers REXO5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises REXO5's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without E2F8 | 0.057 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises REXO5's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without MYBL1 | 0.062 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.0, -48.3); signed map (-44.0, -48.0). **Vector** length 89.1, 18.3% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.67 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.69 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.69 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +18.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.1 | +9.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.6 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -3.7 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA exonuclease 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,806,429-20,849,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NEF-sp |
| Matched by | ensembl_id |

UniProt [Q96IC2](https://www.uniprot.org/uniprotkb/Q96IC2) carries no function annotation.

**Summary**, from NCBI Gene [81691](https://www.ncbi.nlm.nih.gov/gene/81691):

> Predicted to enable exonuclease activity. Predicted to be involved in rRNA 3'-end processing. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24661) · Entrez [81691](https://www.ncbi.nlm.nih.gov/gene/81691) · UniProt [Q96IC2](https://www.uniprot.org/uniprotkb/Q96IC2) · Ensembl [ENSG00000005189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005189)

## Data

Gene col 72: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 72); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 72, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 72]; `tensor/DDL_lfc|DDL_z.npy` [72]; `embed/gene_vectors.npy` [72]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 72 or target_col == 72). Every well: [[REXO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REXO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
