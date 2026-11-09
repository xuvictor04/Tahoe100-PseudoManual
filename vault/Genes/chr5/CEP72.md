---
symbol: "CEP72"
type: "gene"
col: 3415
ensembl_id: "ENSG00000112877"
name: "centrosomal protein 72"
location: "5p15.33"
module: 6
arm: "+"
pooled_cpm: 36.7
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CEP72

*centrosomal protein 72* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.71× (z +7.0, q 8e-10, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.64× (z +6.4, q 2e-08, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.605× (z -9.2, q 2e-17, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX12P]] (+0.68, fdr 7e-06), [[BLM]] (+0.67, fdr 7e-06), [[SPC24]] (+0.66, fdr 1e-05); moves opposite to [[PIGP]] (-0.54, fdr 4e-05), [[MDP1]] (-0.54, fdr 1e-04), [[ZNF407-AS1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.71×** | +7.0 | 8e-10 | 36/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.0 | 8e-10 | 31/47 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.69×** | +6.8 | 2e-09 | 36/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +6.4 | 2e-08 | 33/47 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +6.1 | 2e-07 | 32/48 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +6.0 | 2e-07 | 31/47 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.51×** | +5.3 | 9e-06 | 30/47 (SW480, NCI-H1573, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.6 | 0.020 | 20/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.067 | 12/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.56× | +3.0 | 0.13 | 13/47 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -9.2 | 2e-17 | 36/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.575×** | -7.2 | 2e-10 | 29/43 (COLO 205, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.013 | 22/48 (A-427, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.752×** | -3.7 | 0.030 | 22/48 (Panc 03.27, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.031 | 15/48 (MIA PaCa-2, CHP-212, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.754×** | -3.4 | 0.068 | 19/40 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.699×** | -3.3 | 0.074 | 17/48 (HT-29, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.098 | 15/48 (NCI-H460, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.767× | -3.0 | 0.15 | 18/47 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 67.1 | 3 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.3) |
| [[A-172 (line)]] | wt | 24.5 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.358× (z -9.4) |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (drug)]] 0.05 µM 0.124× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 47.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -8.9) |
| [[COLO 205 (line)]] | alt | 39.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -15.8) |
| [[A-427 (line)]] | wt | 53.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.274× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0784× (z -11.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 36.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.5) |
| [[HOP62 (line)]] | alt | 43.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.9) |
| [[Hs 766T (line)]] | wt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0933× (z -9.0) |
| [[J82 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 40.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX12P]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[BLM]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SPC24]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[DDX11]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FANCB]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CENPI]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[POLE]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[POLD1]] | +0.64 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[FANCA]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CENPK]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[RTEL1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TONSL]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGP]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MDP1]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ZNF407-AS1]] | -0.52 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[RAB21]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[RWDD2B]] | -0.51 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[DHRS4-AS1]] | -0.51 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CEP72's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.3, -46.7); signed map (-38.8, -42.4). **Vector** length 94.2, 20.9% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA replication initiation* (reactome, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.6 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.5 | +7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | -0.0 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.5 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 72 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:612,340-667,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1519, FLJ10565 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P209](https://www.uniprot.org/uniprotkb/Q9P209) (Centrosomal protein of 72 kDa):

> Involved in the recruitment of key centrosomal proteins to the centrosome. Provides centrosomal microtubule-nucleation activity on the gamma-tubulin ring complexes (gamma-TuRCs) and has critical roles in forming a focused bipolar spindle, which is needed for proper tension generation between sister chromatids. Required for localization of KIZ, AKAP9 and gamma-tubulin ring complexes (gamma-TuRCs). Involved in centriole duplication. Required for CDK5RAP22, CEP152, WDR62 and CEP63 centrosomal …

**Summary**, from NCBI Gene [55722](https://www.ncbi.nlm.nih.gov/gene/55722):

> The product of this gene is a member of the leucine-rich-repeat (LRR) superfamily of proteins. The protein is localized to the centrosome, a non-membraneous organelle that functions as the major microtubule-organizing center in animal cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25547) · Entrez [55722](https://www.ncbi.nlm.nih.gov/gene/55722) · UniProt [Q9P209](https://www.uniprot.org/uniprotkb/Q9P209) · Ensembl [ENSG00000112877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112877)

## Data

Gene col 3415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3415); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3415]; `tensor/DDL_lfc|DDL_z.npy` [3415]; `embed/gene_vectors.npy` [3415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3415 or target_col == 3415). Every well: [[CEP72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
