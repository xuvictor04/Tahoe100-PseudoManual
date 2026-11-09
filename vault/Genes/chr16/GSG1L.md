---
symbol: "GSG1L"
type: "gene"
col: 9766
ensembl_id: "ENSG00000169181"
name: "GSG1 like"
location: "16p12.1"
module: 53
arm: "+"
pooled_cpm: 3.12
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# GSG1L

*GSG1 like* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.44× (z +18.7, q 0e+00, up in 25 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.621× (z -5.1, q 2e-04, down in 8 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELF5]] (+0.73, fdr 7e-06), [[CATSPERD]] (+0.72, fdr 7e-06), [[KIF17]] (+0.68, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.44×** | +18.7 | 0e+00 | 25/35 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.27×** | +14.9 | 0e+00 | 2/2 (J82, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +13.9 | 8e-42 | 28/34 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.42×** | +13.1 | 3e-37 | 35/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +12.4 | 3e-33 | 4/14 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +10.6 | 4e-24 | 23/44 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +8.5 | 1e-15 | 20/39 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.57×** | +8.5 | 1e-15 | 23/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +8.2 | 2e-14 | 22/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.7 | 9e-10 | 14/34 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +6.6 | 2e-09 | 19/43 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +6.3 | 1e-08 | 11/44 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +5.7 | 4e-07 | 14/38 (SNU-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.4 | 3e-06 | 2/5 (A498, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 9e-04 | 9/37 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.004 | 3/28 (RPMI-7951, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +3.7 | 0.005 | 6/29 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.009 | 4/42 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.621×** | -5.1 | 2e-04 | 8/43 (SW48, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -4.4 | 0.003 | 16/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.470×** | -4.2 | 0.004 | 6/26 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.784×** | -3.7 | 0.031 | 11/42 (Hs 766T, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.696× | -3.3 | 0.12 | 9/43 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.568× | -3.2 | 0.14 | 4/39 (LS 180, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.10 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.85× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.135× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 15.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -11.6) |
| [[HCT15 (line)]] | alt | 6.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 6.07 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0874× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 2.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 3.47 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.05 µM 0.0626× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 1.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 3.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +10.0) | — |
| [[A-172 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.906 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF5]] | +0.73 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[KIF17]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CACNA1E]] | +0.64 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.64 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[IRAG1-AS1]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[LINC01811]] | +0.63 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[CAMK2B]] | +0.63 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[CPNE9]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PLB1]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADRA2C]] | B | ADRA2C activity raises GSG1L's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without ADRA2C | 0.037 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[SRC]] | B | SRC activity raises GSG1L's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, -14.4); signed map (20.9, 13.8). **Vector** length 56.4, 8.08% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[NG25 (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | GSG1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:27,787,528-28,063,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC18079, PRO19651, KTSR5831 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXU4](https://www.uniprot.org/uniprotkb/Q6UXU4) (Germ cell-specific gene 1-like protein):

> As a component of the inner core of AMPAR complex, modifies AMPA receptor (AMPAR) gating.

**Summary**, from NCBI Gene [146395](https://www.ncbi.nlm.nih.gov/gene/146395):

> Predicted to be involved in regulation of cell communication; regulation of postsynaptic neurotransmitter receptor internalization; and regulation of signaling. Predicted to act upstream of or within several processes, including regulation of AMPA receptor activity; regulation of short-term neuronal synaptic plasticity; and transmission of nerve impulse. Predicted to be located in asymmetric synapse and membrane. Predicted to be active in postsynaptic density membrane. [provided by Alliance of …

**Accessions** — [HGNC:28283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28283) · Entrez [146395](https://www.ncbi.nlm.nih.gov/gene/146395) · UniProt [Q6UXU4](https://www.uniprot.org/uniprotkb/Q6UXU4) · Ensembl [ENSG00000169181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169181)

## Data

Gene col 9766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9766); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9766]; `tensor/DDL_lfc|DDL_z.npy` [9766]; `embed/gene_vectors.npy` [9766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9766 or target_col == 9766). Every well: [[GSG1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSG1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
