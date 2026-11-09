---
symbol: "SARS2"
type: "gene"
col: 2504
ensembl_id: "ENSG00000104835"
name: "seryl-tRNA synthetase 2, mitochondrial"
location: "19q13.2"
module: 4
arm: "+"
pooled_cpm: 6.6
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SARS2

*seryl-tRNA synthetase 2, mitochondrial* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.63× (z +6.2, q 4e-07, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.54× (z +5.4, q 2e-05, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.454× (z -10.1, q 4e-21, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS27]] (+0.71, fdr 7e-06), [[NAA25]] (+0.71, fdr 7e-06), [[CLPB]] (+0.68, fdr 7e-06); moves opposite to [[MINDY2]] (-0.64, fdr 1e-05), [[PLAG1]] (-0.59, fdr 1e-05), [[CERT1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.2 | 4e-07 | 4/7 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +5.4 | 2e-05 | 14/44 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.0 | 1e-04 | 15/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 6e-04 | 13/45 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.2 | 0.003 | 5/25 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.0 | 0.006 | 3/21 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.8 | 0.010 | 3/18 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.022 | 6/46 (PANC-1, SHP-77, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.2 | 0.077 | 2/14 (NCI-H2030, PANC-1) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.082 | 9/44 (LoVo, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -10.1 | 4e-21 | 26/38 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -8.8 | 3e-16 | 28/42 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -8.5 | 4e-15 | 23/40 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -6.1 | 1e-07 | 20/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -6.1 | 2e-07 | 21/44 (HEC-1-A, A-427, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.646×** | -5.8 | 6e-07 | 17/46 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.652×** | -5.7 | 1e-06 | 18/46 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.664×** | -5.5 | 4e-06 | 20/45 (SW48, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -5.4 | 4e-06 | 19/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.678×** | -5.2 | 1e-05 | 18/46 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -4.9 | 4e-05 | 17/47 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.719×** | -4.4 | 5e-04 | 15/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -4.3 | 6e-04 | 10/46 (AN3 CA, HOP62, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.742×** | -4.0 | 0.003 | 8/45 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.004 | 8/46 (A549, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 6 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 5.12 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0804× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.112× (z -9.0) |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 2 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0902× (z -9.0) |
| [[SW48 (line)]] | wt | 7.38 | 0 | 2 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0472× (z -9.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0712× (z -8.5) |
| [[COLO 205 (line)]] | alt | 8.60 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0844× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 6.58 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.158× (z -8.8) |
| [[HOP62 (line)]] | alt | 4.81 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0985× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 7.85 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0955× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 5.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -8.7) |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -11.4) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.2) |
| [[A-172 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS27]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[NAA25]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[CLPB]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[MINDY4]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[DCAF1]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[USP5]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CCT2]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[E2F6]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[OGFOD3]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[INTS7]] | +0.63 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[VWA8]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[COX10]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY2]] | -0.64 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CERT1]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[UBXN7]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[KATNA1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[OPTN]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZNF654]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SARS2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.0, -32.9); signed map (-11.3, -47.8). **Vector** length 63.5, 9.20% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -8.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.4 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | seryl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,915,266-38,930,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20450, mtSerRS, SerRSmt, SARS, SERS, SYS; previously SARSM |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP81](https://www.uniprot.org/uniprotkb/Q9NP81) (Serine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of serine to tRNA(Ser). Is also probably able to aminoacylate tRNA(Sec) with serine, to form the misacylated tRNA L-seryl-tRNA(Sec), which will be further converted into selenocysteinyl-tRNA(Sec).

**Summary**, from NCBI Gene [54938](https://www.ncbi.nlm.nih.gov/gene/54938):

> This gene encodes the mitochondrial seryl-tRNA synthethase precursor, a member of the class II tRNA synthetase family. The mature enzyme catalyzes the ligation of Serine to tRNA(Ser) and participates in the biosynthesis of selenocysteinyl-tRNA(sec) in mitochondria. The enzyme contains an N-terminal tRNA binding domain and a core catalytic domain. It functions in a homodimeric form, which is stabilized by tRNA binding. This gene is regulated by a bidirectional promoter that also controls the …

**Accessions** — [HGNC:17697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17697) · Entrez [54938](https://www.ncbi.nlm.nih.gov/gene/54938) · UniProt [Q9NP81](https://www.uniprot.org/uniprotkb/Q9NP81) · Ensembl [ENSG00000104835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104835)

## Data

Gene col 2504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2504); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2504]; `tensor/DDL_lfc|DDL_z.npy` [2504]; `embed/gene_vectors.npy` [2504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2504 or target_col == 2504). Every well: [[SARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
