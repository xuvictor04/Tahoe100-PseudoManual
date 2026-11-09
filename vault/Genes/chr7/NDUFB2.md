---
symbol: "NDUFB2"
type: "gene"
col: 1615
ensembl_id: "ENSG00000090266"
name: "NADH:ubiquinone oxidoreductase subunit B2"
location: "7q34"
module: 48
arm: "+"
pooled_cpm: 42.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFB2

*NADH:ubiquinone oxidoreductase subunit B2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +9.3, q 6e-18, up in 42 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1792 6.40×, C32 4.45×, A549 4.79×, NCI-H23 4.05×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -6.8, q 8e-09, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA13]] (+0.72, fdr 1e-05, ⚠ NDUFA13 in the vector space only through flagged drug-doses), [[COPS9]] (+0.66, fdr 7e-06), [[NENF]] (+0.63, fdr 7e-06), [[NDUFA1]] (+0.62, fdr 1e-05); moves opposite to [[NELFE]] (-0.60, fdr 1e-04), [[BACE1-AS]] (-0.53, fdr 3e-05), [[CSRP1]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRFN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1792 6.40×, C32 4.45×, A549 4.79×, NCI-H23 4.05×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 6.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +9.3 | 6e-18 | 42/46 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.29×** | +6.6 | 9e-09 | 32/39 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +6.0 | 4e-07 | 42/46 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.81×** | +4.6 | 7e-04 | 31/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.63×** | +4.1 | 0.005 | 36/47 (SW480, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.53×** | +3.6 | 0.035 | 32/47 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.2 | 0.13 | 26/47 (RKO, NCI-H2030, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.45× | +3.1 | 0.13 | 26/48 (SW1417, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -6.8 | 8e-09 | 46/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -4.4 | 0.003 | 32/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.614×** | -4.0 | 0.010 | 36/48 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.052 | 31/48 (MIA PaCa-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.654× | -3.2 | 0.13 | 36/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.667× | -3.1 | 0.19 | 30/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 39.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -8.6) |
| [[A-427 (line)]] | wt | 48.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.1) |
| [[A549 (line)]] | wt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 81.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 60.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.1) |
| [[SNU-423 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 12 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA13]] ⚠ | +0.72 | +0.53 / +0.76 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[COPS9]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NENF]] | +0.63 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[NDUFA1]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[UQCR11]] | +0.62 | +0.64 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 937 |
| [[C1orf122]] | +0.62 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[MIR762HG]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[MZT2A]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NDUFB11]] ⚠ | +0.60 | +0.56 / +0.63 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | +0.59 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[NDUFAF8]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[NDUFB1]] | +0.59 | +0.34 / +0.65 | both halves | 1e-04 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[ATOX1]] | +0.59 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.58 | +0.64 / +0.47 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NELFE]] | -0.60 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[BACE1-AS]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CSRP1]] | -0.52 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[PDAP1]] | -0.52 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[RLIM]] | -0.51 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.51 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[MRPS10]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[HUWE1]] | -0.50 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN4]] | B | LRFN4 activity raises NDUFB2's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without LRFN4 | 0.012 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[HDAC6]] | B | HDAC6 activity raises NDUFB2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.5, -21.7); signed map (-36.4, 9.0). **Vector** length 63.1, 19.1% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.51 to 7); *Cristae formation* (reactome, mean cos +0.51 to 7); *Mitochondrial biogenesis* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.3 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -4.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,690,777-140,722,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AGGG, CI-AGGG |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95178](https://www.uniprot.org/uniprotkb/O95178) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4708](https://www.ncbi.nlm.nih.gov/gene/4708):

> The protein encoded by this gene is a subunit of the multisubunit NADH:ubiquinone oxidoreductase (complex I). Mammalian complex I is composed of 45 different subunits. This protein has NADH dehydrogenase activity and oxidoreductase activity. It plays a important role in transfering electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Hydropathy analysis revealed that this subunit and 4 other subunits have an overall …

**Accessions** — [HGNC:7697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7697) · Entrez [4708](https://www.ncbi.nlm.nih.gov/gene/4708) · UniProt [O95178](https://www.uniprot.org/uniprotkb/O95178) · Ensembl [ENSG00000090266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090266)

## Data

Gene col 1615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1615); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1615]; `tensor/DDL_lfc|DDL_z.npy` [1615]; `embed/gene_vectors.npy` [1615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1615 or target_col == 1615). Every well: [[NDUFB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
