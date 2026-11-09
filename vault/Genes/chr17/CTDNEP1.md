---
symbol: "CTDNEP1"
type: "gene"
col: 10654
ensembl_id: "ENSG00000175826"
name: "CTD nuclear envelope phosphatase 1"
location: "17p13.1"
module: 157
arm: "+"
pooled_cpm: 20.56
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# CTDNEP1

*CTD nuclear envelope phosphatase 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.77× (z +8.1, q 3e-13, up in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.54× (z +4.4, q 9e-04, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -7.7, q 8e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHPS]] (+0.59, fdr 7e-06), [[NAPA-AS1]] (+0.56, fdr 1e-04), [[SCAMP4]] (+0.55, fdr 5e-05); moves opposite to [[HSP90AB1]] (-0.50, fdr 9e-05), [[EFL1]] (-0.48, fdr 2e-04), [[HSP90AA1]] (-0.46, fdr 5e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +8.1 | 3e-13 | 29/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.8 | 2e-12 | 35/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.3 | 6e-11 | 24/33 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.55×** | +6.1 | 1e-07 | 26/45 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.52×** | +5.9 | 3e-07 | 27/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.2 | 2e-05 | 2/48 (HOP62, HCT15) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.8 | 2e-04 | 17/36 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +4.4 | 9e-04 | 17/47 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.008 | 19/45 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.010 | 13/44 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.30×** | +3.7 | 0.011 | 17/47 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.37×** | +3.6 | 0.016 | 17/46 (NCI-H23, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.017 | 16/48 (hTERT-HPNE, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +3.4 | 0.025 | 17/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.26×** | +3.2 | 0.050 | 12/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.056 | 10/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.082 | 16/46 (LoVo, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -7.7 | 8e-12 | 38/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -7.6 | 1e-11 | 36/47 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -6.9 | 7e-10 | 36/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.715×** | -4.8 | 3e-04 | 22/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -4.7 | 3e-04 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.805×** | -4.4 | 0.001 | 22/47 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.523×** | -3.7 | 0.019 | 15/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.6 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.35× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.137× (z -10.8) |
| [[C32 (line)]] | wt | 11.2 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0462× (z -11.0) |
| [[HOP62 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.2) ⚠ cell-cycle shift, explains ~16% of this change |
| [[RKO (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.0) |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.8) |
| [[A-172 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHPS]] | +0.59 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NAPA-AS1]] | +0.56 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[SCAMP4]] | +0.55 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[LAMB2]] | +0.53 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[ZNF580]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[AKT2]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[POLDIP3]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[DVL2]] | +0.52 | +0.44 / +0.59 | both halves | 3e-05 | ⚠ same locus (9.1 kb, same strand: neighbours can correlate without regulation) |
| [[VARS2]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[TRIM28]] | +0.52 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[PTOV1]] | +0.51 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MIB2]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TM9SF1]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB1]] | -0.50 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[EFL1]] | -0.48 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[HSP90AA1]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PPID]] | -0.45 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[SMS]] | -0.44 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[HSPD1]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[CSNK1G3]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DYNLT3]] | -0.43 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[SH3KBP1]] | -0.42 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[SNX10]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[CCT6A]] | -0.41 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[NRIP3]] | -0.41 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CTDNEP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CTDNEP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.6, -44.5); signed map (2.5, -5.8). **Vector** length 54.2, 8.76% of its response variance represented; |z| ≥ 3 in 622 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.4 | +5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +7.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.6 | +3.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +4.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | CTD nuclear envelope phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,243,591-7,252,491 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSA011916, NET56; previously DULLARD |
| Gene groups (HGNC) | CTD family phosphatases |
| Reactome | 6 pathways, smallest: Depolymerization of the Nuclear Lamina; Nuclear Envelope Breakdown; Mitotic Prophase |
| Matched by | ensembl_id |

**Function**, from UniProt [O95476](https://www.uniprot.org/uniprotkb/O95476) (CTD nuclear envelope phosphatase 1):

> Serine/threonine protein phosphatase forming with CNEP1R1 an active phosphatase complex that dephosphorylates and may activate LPIN1 and LPIN2. LPIN1 and LPIN2 are phosphatidate phosphatases that catalyze the conversion of phosphatidic acid to diacylglycerol and control the metabolism of fatty acids at different levels. May indirectly modulate the lipid composition of nuclear and/or endoplasmic reticulum membranes and be required for proper nuclear membrane morphology and/or dynamics. May also …

**Summary**, from NCBI Gene [23399](https://www.ncbi.nlm.nih.gov/gene/23399):

> Enables protein serine/threonine phosphatase activity. Involved in several processes, including positive regulation of triglyceride biosynthetic process; protein dephosphorylation; and protein localization to nucleus. Located in endoplasmic reticulum membrane and nuclear membrane. Part of Nem1-Spo7 phosphatase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19085) · Entrez [23399](https://www.ncbi.nlm.nih.gov/gene/23399) · UniProt [O95476](https://www.uniprot.org/uniprotkb/O95476) · Ensembl [ENSG00000175826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175826)

## Data

Gene col 10654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10654); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10654]; `tensor/DDL_lfc|DDL_z.npy` [10654]; `embed/gene_vectors.npy` [10654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10654 or target_col == 10654). Every well: [[CTDNEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTDNEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
