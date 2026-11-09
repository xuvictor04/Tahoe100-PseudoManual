---
symbol: "ARFGAP2"
type: "gene"
col: 7347
ensembl_id: "ENSG00000149182"
name: "ARF GTPase activating protein 2"
location: "11p11.2"
module: 173
arm: "+"
pooled_cpm: 21.74
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# ARFGAP2

*ARF GTPase activating protein 2* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +19.0, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.670× (z -10.3, q 3e-22, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEF1]] (+0.79, fdr 7e-06), [[MED12]] (+0.75, fdr 7e-06), [[BRPF3]] (+0.75, fdr 7e-06); moves opposite to [[SNRPD2]] (-0.70, fdr 1e-05), [[PCMT1]] (-0.69, fdr 4e-05), [[FCHO1]] (-0.66, fdr 4e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +19.0 | 0e+00 | 43/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +13.8 | 1e-40 | 42/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +10.6 | 8e-24 | 40/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +10.5 | 2e-23 | 40/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +7.5 | 5e-12 | 36/48 (A498, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.5 | 6e-12 | 28/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.1 | 1e-10 | 32/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.0 | 1e-07 | 24/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.8 | 4e-07 | 22/46 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 3e-05 | 20/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +4.1 | 0.002 | 17/37 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 15/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.010 | 17/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 8/48 (A498, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.038 | 13/47 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.0 | 0.093 | 6/47 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.670×** | -10.3 | 3e-22 | 43/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.598×** | -9.4 | 1e-18 | 35/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.609×** | -9.1 | 3e-17 | 33/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -8.3 | 2e-14 | 37/47 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.640×** | -8.1 | 4e-14 | 37/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.650×** | -7.9 | 4e-13 | 32/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -5.5 | 3e-06 | 23/47 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.780×** | -4.5 | 4e-04 | 20/47 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.805×** | -4.0 | 0.005 | 13/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.005 | 11/48 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 32.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +18.3) | — |
| [[A498 (line)]] | wt | 22.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 23.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 33.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.7) | — |
| [[A-172 (line)]] | wt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.4) | — |
| [[A549 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0833× (z -8.9) |
| [[COLO 205 (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.284× (z -9.1) |
| [[SW480 (line)]] | alt | 27.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.8) | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEF1]] | +0.79 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[MED12]] | +0.75 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[BRPF3]] | +0.75 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.73 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.70 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.70 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[EIF2B5]] | +0.70 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.70 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TIA1]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[VPS52]] | +0.69 | +0.61 / +0.52 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[UBE3B]] | +0.69 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD2]] | -0.70 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PCMT1]] | -0.69 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[FCHO1]] | -0.66 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.64 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ETHE1]] | -0.64 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.64 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[LPCAT2]] | -0.64 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[COG5]] | -0.63 | -0.65 / -0.36 | both halves | 1e-04 | pathway: Asparagine N-linked glycosylation |
| [[YIF1B]] | -0.63 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.63 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[PIBF1]] | -0.63 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ABHD6]] | -0.62 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ARFGAP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ARFGAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.0, 4.9); signed map (16.2, -22.5). **Vector** length 89.2, 18.3% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +19.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -10.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.4 | -8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase activating protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,164,299-47,177,125 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRZ, Zfp289, FLJ14576; previously ZNF289 |
| Gene groups (HGNC) | ArfGAPs |
| Reactome | 13 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6H7](https://www.uniprot.org/uniprotkb/Q8N6H7) (ADP-ribosylation factor GTPase-activating protein 2):

> GTPase-activating protein (GAP) for ADP ribosylation factor 1 (ARF1), which is essential for COPI vesicle formation and retrograde transport between the Golgi and the endoplasmic reticulum. Hydrolysis of ARF1-bound GTP leads to dissociation of coatomer from Golgi-derived membranes to allow fusion with target membranes. Promotes the proper assembly of the COPI coat lattice, rather than just acting as a simple curvature-dependent GAP like ARFGAP1. Also acts as a regulator of STING1 activity, both …

**Summary**, from NCBI Gene [84364](https://www.ncbi.nlm.nih.gov/gene/84364):

> Predicted to enable GTPase activator activity. Predicted to be involved in COPI coating of Golgi vesicle. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13504) · Entrez [84364](https://www.ncbi.nlm.nih.gov/gene/84364) · UniProt [Q8N6H7](https://www.uniprot.org/uniprotkb/Q8N6H7) · Ensembl [ENSG00000149182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149182)

## Data

Gene col 7347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7347); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7347]; `tensor/DDL_lfc|DDL_z.npy` [7347]; `embed/gene_vectors.npy` [7347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7347 or target_col == 7347). Every well: [[ARFGAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFGAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
