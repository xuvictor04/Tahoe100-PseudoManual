---
symbol: "BNIP1"
type: "gene"
col: 3497
ensembl_id: "ENSG00000113734"
name: "BCL2 interacting protein 1"
location: "5q35.1"
module: 12
arm: "+"
pooled_cpm: 15.84
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# BNIP1

*BCL2 interacting protein 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +12.9, q 2e-35, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.96× (z +10.2, q 6e-22, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.614× (z -6.6, q 2e-08, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VIRMA]] (+0.70, fdr 2e-05), [[KBTBD7]] (+0.66, fdr 1e-05), [[DRG1]] (+0.63, fdr 5e-05); moves opposite to [[DIAPH1]] (-0.61, fdr 1e-05), [[CDK2]] (-0.56, fdr 1e-04), [[FKBP1A]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.90×** | +12.9 | 2e-35 | 39/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.96×** | +10.2 | 6e-22 | 43/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.0 | 3e-17 | 36/47 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +8.4 | 1e-14 | 41/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.80×** | +8.0 | 1e-13 | 36/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.5 | 4e-12 | 29/45 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +7.0 | 2e-10 | 34/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +6.2 | 4e-08 | 32/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +5.5 | 2e-06 | 24/45 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.47×** | +5.5 | 3e-06 | 26/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +5.3 | 5e-06 | 22/38 (NCI-H23, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.001 | 21/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.1 | 0.002 | 20/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +3.4 | 0.023 | 14/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.1 | 0.077 | 11/47 (SNU-423, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -6.6 | 2e-08 | 26/46 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -5.6 | 6e-06 | 27/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.5 | 7e-06 | 25/48 (NCI-H2030, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.728×** | -4.5 | 1e-03 | 18/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.754×** | -4.0 | 0.007 | 17/48 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.0 | 0.007 | 18/48 (NCI-H23, CHP-212, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.792×** | -3.3 | 0.074 | 11/47 (AsPC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.1 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Panobinostat (drug)]] 5 µM 0.252× (z -11.3) |
| [[A-172 (line)]] | wt | 12.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +10.2) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.196× (z -10.3) |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 1 | — | [[Captopril (drug)]] 0.5 µM 0.0687× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 15.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.2) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +10.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIRMA]] | +0.70 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[KBTBD7]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[DRG1]] | +0.63 | +0.76 / +0.39 | both halves | 5e-05 |  |
| [[CCDC174]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ZRSR2]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TP53BP1]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[UFL1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NFKBIL1]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MYNN]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PCGF1]] ⚠ | +0.61 | +0.62 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GOSR1]] | +0.60 | +0.68 / +0.44 | both halves | 3e-05 | same gene group; pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 879 |
| [[RP9]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CIR1]] | +0.60 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CDK2]] | -0.56 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[FKBP1A]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.53 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[ITGB1]] | -0.52 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[SNTB2]] | -0.52 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[TTL]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MAPK1]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BNIP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises BNIP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises BNIP1's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.6, -6.7); signed map (-14.6, -9.6). **Vector** length 72.2, 13.3% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.0 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +9.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.4 | +8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | -1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.8 | +5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -5.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:173,144,442-173,164,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nip1, SEC20 |
| Gene groups (HGNC) | SNAREs; BCL2 homology region 3 (BH3) only |
| Reactome | 5 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12981](https://www.uniprot.org/uniprotkb/Q12981) (Vesicle transport protein SEC20):

> As part of a SNARE complex may be involved in endoplasmic reticulum membranes fusion and be required for the maintenance of endoplasmic reticulum organization. Also plays a role in apoptosis. It is for instance required for endoplasmic reticulum stress-induced apoptosis. As a substrate of RNF185 interacting with SQSTM1, might also be involved in mitochondrial autophagy (Probable).

**Summary**, from NCBI Gene [662](https://www.ncbi.nlm.nih.gov/gene/662):

> This gene is a member of the BCL2/adenovirus E1B 19 kd-interacting protein (BNIP) family. It interacts with the E1B 19 kDa protein, which protects cells from virally-induced cell death. The encoded protein also interacts with E1B 19 kDa-like sequences of BCL2, another apoptotic protector. In addition, this protein is involved in vesicle transport into the endoplasmic reticulum. Alternative splicing of this gene results in four protein products with identical N- and C-termini. [provided by …

**Accessions** — [HGNC:1082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1082) · Entrez [662](https://www.ncbi.nlm.nih.gov/gene/662) · UniProt [Q12981](https://www.uniprot.org/uniprotkb/Q12981) · Ensembl [ENSG00000113734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113734)

## Data

Gene col 3497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3497); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3497]; `tensor/DDL_lfc|DDL_z.npy` [3497]; `embed/gene_vectors.npy` [3497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3497 or target_col == 3497). Every well: [[BNIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
