---
symbol: "BCAT2"
type: "gene"
col: 2618
ensembl_id: "ENSG00000105552"
name: "branched chain amino acid transaminase 2"
location: "19q13.33"
module: 29
arm: "-"
pooled_cpm: 24.58
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# BCAT2

*branched chain amino acid transaminase 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +7.9, q 2e-12, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.597× (z -9.1, q 4e-17, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3A]] (+0.64, fdr 3e-05), [[INAFM1]] (+0.61, fdr 1e-05), [[MARCHF9]] (+0.59, fdr 1e-05); moves opposite to [[TOR1A]] (-0.66, fdr 1e-05), [[SUMO3]] (-0.61, fdr 3e-05), [[MOB1A]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANTXR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-12 | 23/46 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.2 | 5e-05 | 23/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +4.5 | 0.001 | 19/46 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 0.001 | 22/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.012 | 12/45 (NCI-H460, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.21× | +3.2 | 0.14 | 15/45 (C-33 A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -9.1 | 4e-17 | 31/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -8.7 | 1e-15 | 31/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -7.7 | 2e-12 | 29/47 (HT-29, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -7.6 | 5e-12 | 35/47 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -7.5 | 9e-12 | 26/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -7.4 | 1e-11 | 28/44 (Panc 03.27, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -7.3 | 2e-11 | 29/46 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -6.8 | 8e-10 | 30/47 (HT-29, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -5.8 | 4e-07 | 23/47 (SNU-423, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -5.5 | 3e-06 | 24/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -5.0 | 3e-05 | 3/47 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.819×** | -5.0 | 3e-05 | 25/46 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -4.2 | 1e-03 | 20/38 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.634×** | -4.2 | 0.001 | 17/41 (SK-MEL-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.005 | 16/46 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.809×** | -3.7 | 0.006 | 15/47 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -3.0 | 0.080 | 11/47 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 20.0 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 3.44× (z +8.5) | [[Bortezomib (drug)]] 0.05 µM 0.219× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 55.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -8.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[RPMI-7951 (line)]] | alt | 37.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.4) | — |
| [[A549 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -8.6) |
| [[LoVo (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.0) ⚠ cell-cycle shift, explains ~8% of this change |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0738× (z -8.7) |
| [[LS 180 (line)]] | wt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.404× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0802× (z -9.0) |
| [[PANC-1 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.363× (z -8.5) |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -11.8) |
| [[A-427 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3A]] | +0.64 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[INAFM1]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[MARCHF9]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[EML2]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CFDP1]] | +0.58 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[CAMKK1]] | +0.57 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[AFMID]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[VEGFB]] | +0.56 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PDP2]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[CROCCP2-1]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZMYM6]] | +0.56 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1A]] | -0.66 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.61 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.59 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[XRCC6]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[STX16]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.57 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[CRPPA]] | -0.56 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[PDIA3P1]] | -0.55 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[ARSB]] | -0.55 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[EIF4G2]] | -0.55 | -0.22 / -0.63 | both halves | 6e-04 |  |
| [[TSPAN6]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANTXR1]] | B | ANTXR1 activity raises BCAT2's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without ANTXR1 | 0.031 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[HDAC6]] | B | HDAC6 activity lowers BCAT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-32.3, -26.2); signed map (-26.3, 14.4). **Vector** length 83.4, 16.0% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.8 | +0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -6.0 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -4.2 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -7.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | branched chain amino acid transaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,795,062-48,811,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCAM, BCATm; previously BCT2 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Branched chain amino acid transaminase family |
| Reactome | 2 pathways, smallest: Branched-chain amino acid catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O15382](https://www.uniprot.org/uniprotkb/O15382) (Branched-chain-amino-acid aminotransferase, mitochondrial):

> Catalyzes the first reaction in the catabolism of the essential branched chain amino acids leucine, isoleucine, and valine. Branched chain amino acid catabolism plays a role in adipocyte differentiation by providing lipogenic acetyl-CoA pools in differentiated adipocytes (By similarity). Mechanistically, acetyl-CoA derived from branched chain amino acid catabolism is used by EP300/p300 to acetylate and inhibit PRDM16, thereby preventing adipose tissue browning (By similarity). May also function …

**Summary**, from NCBI Gene [587](https://www.ncbi.nlm.nih.gov/gene/587):

> This gene encodes a branched chain aminotransferase found in mitochondria. The encoded protein forms a dimer that catalyzes the first step in the production of the branched chain amino acids leucine, isoleucine, and valine. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:977) · Entrez [587](https://www.ncbi.nlm.nih.gov/gene/587) · UniProt [O15382](https://www.uniprot.org/uniprotkb/O15382) · Ensembl [ENSG00000105552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105552)

## Data

Gene col 2618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2618); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2618]; `tensor/DDL_lfc|DDL_z.npy` [2618]; `embed/gene_vectors.npy` [2618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2618 or target_col == 2618). Every well: [[BCAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
