---
symbol: "SPON2"
type: "gene"
col: 8267
ensembl_id: "ENSG00000159674"
name: "spondin 2"
location: "4p16.3"
module: 47
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SPON2

*spondin 2* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +9.0, q 2e-16, up in 5 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.54× (z +5.4, q 2e-05, up in 15 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.420× (z -9.5, q 8e-19, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf38]] (+0.69, fdr 7e-06), [[KIF17]] (+0.68, fdr 7e-06), [[MYO15A]] (+0.67, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LSMEM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +9.0 | 2e-16 | 5/13 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.4 | 2e-05 | 6/45 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +5.4 | 2e-05 | 15/37 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.7 | 4e-04 | 5/22 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 7e-04 | 15/36 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.2 | 0.002 | 3/15 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.051 | 7/43 (SW480, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +3.4 | 0.051 | 6/32 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.051 | 10/34 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.098 | 6/41 (LOX-IMVI, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -9.5 | 8e-19 | 31/44 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.484×** | -8.0 | 4e-13 | 23/41 (RPMI-7951, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -7.4 | 3e-11 | 22/33 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -6.7 | 3e-09 | 19/38 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -5.0 | 5e-05 | 15/41 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -4.4 | 9e-04 | 18/41 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.705×** | -3.9 | 0.009 | 9/43 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -3.7 | 0.018 | 11/40 (SW1417, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.744×** | -3.3 | 0.066 | 15/43 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.745×** | -3.2 | 0.066 | 10/39 (COLO 205, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0957× (z -11.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 7.72 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.101× (z -9.2) |
| [[BT-474 (line)]] | alt | 9.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0694× (z -10.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 6.06 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0865× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0799× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.66 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -9.7) |
| [[A-172 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf38]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KIF17]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[HPN]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ATP2A1]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[RFPL3S]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSMEM2]] | B | LSMEM2 activity raises SPON2's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without LSMEM2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises SPON2's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without SEMA4A | 0.093 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[GAL3ST1]] | B | GAL3ST1 activity raises SPON2's level | lines that do not express GAL3ST1 (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without GAL3ST1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| [[AXDND1]] | C | AXDND1 activity lowers SPON2's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 2.61× higher at baseline in the lines without AXDND1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.2, -17.1); signed map (18.1, 13.0). **Vector** length 60.6, 8.59% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -7.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | spondin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,166,932-1,208,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIL1 |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUD6](https://www.uniprot.org/uniprotkb/Q9BUD6) (Spondin-2):

> Cell adhesion protein that promotes adhesion and outgrowth of hippocampal embryonic neurons. Binds directly to bacteria and their components and functions as an opsonin for macrophage phagocytosis of bacteria. Essential in the initiation of the innate immune response and represents a unique pattern-recognition molecule in the ECM for microbial pathogens (By similarity). Binds bacterial lipopolysaccharide (LPS).

**Summary**, from NCBI Gene [10417](https://www.ncbi.nlm.nih.gov/gene/10417):

> Predicted to enable antigen binding activity; lipopolysaccharide binding activity; and metal ion binding activity. Predicted to be involved in cell adhesion. Predicted to act upstream of or within several processes, including opsonization; positive regulation of cytokine production; and response to bacterium. Located in extracellular exosome. Biomarker of meningioma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11253) · Entrez [10417](https://www.ncbi.nlm.nih.gov/gene/10417) · UniProt [Q9BUD6](https://www.uniprot.org/uniprotkb/Q9BUD6) · Ensembl [ENSG00000159674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159674)

## Data

Gene col 8267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8267); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8267]; `tensor/DDL_lfc|DDL_z.npy` [8267]; `embed/gene_vectors.npy` [8267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8267 or target_col == 8267). Every well: [[SPON2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPON2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
