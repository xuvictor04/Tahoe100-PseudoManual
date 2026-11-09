---
symbol: "PSMG2"
type: "gene"
col: 4920
ensembl_id: "ENSG00000128789"
name: "proteasome assembly chaperone 2"
location: "18p11.21"
module: 178
arm: "+"
pooled_cpm: 40.72
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# PSMG2

*proteasome assembly chaperone 2* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 1.56× (z +5.7, q 7e-06, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.714× (z -11.6, q 4e-28, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGPA]] (+0.58, fdr 3e-05), [[RPP30]] (+0.56, fdr 3e-05), [[MANEAL]] (+0.56, fdr 4e-05); moves opposite to [[TEX14]] (-0.55, fdr 2e-05), [[RELT]] (-0.54, fdr 1e-05), [[CYCS]] (-0.53, fdr 2e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FRG1DP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +5.7 | 7e-06 | 26/47 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +5.4 | 2e-05 | 21/48 (KATO III, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +4.1 | 0.007 | 16/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.024 | 13/46 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.027 | 19/46 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Sonidegib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.13 | 9/48 (SNU-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.20 | 15/48 (J82, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.714×** | -11.6 | 4e-28 | 34/48 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.762×** | -6.3 | 6e-08 | 27/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -5.1 | 5e-05 | 17/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -4.7 | 4e-04 | 15/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.883× | -4.3 | 0.002 | 21/48 (SW48, LS 180, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -4.2 | 0.003 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.869× | -3.4 | 0.063 | 6/48 (SW48, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.871× | -3.2 | 0.095 | 16/47 (SW48, A-172, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.878× | -3.2 | 0.10 | 8/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 60.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.0) |
| [[SW48 (line)]] | wt | 108 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -12.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.9) |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.278× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 52.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.2) |
| [[A-172 (line)]] | wt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.0) |
| [[HOP62 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.174× (z -11.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 66.7 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0620× (z -12.5) |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGPA]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[RPP30]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[MANEAL]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[STX18]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TMEM161B]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ORC5]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SDHB]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CROT]] | +0.54 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[ASB7]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RTCA]] | +0.53 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TENT2]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CDC40]] | +0.53 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX14]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[RELT]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CYCS]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[LINC00910]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CCDC200]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DELEC1]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[INTS6]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[COL7A1]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[HCG20]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[FUS]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[SH2D4B]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1DP]] | B | FRG1DP activity lowers PSMG2's level | lines that do not express FRG1DP (17) vs lines expressing it (33) | 1.32× higher at baseline in the lines without FRG1DP | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000237596, C9, GLIPR1 |
| [[DELEC1]] | B | DELEC1 activity lowers PSMG2's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without DELEC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.9, -12.2); signed map (-33.1, -18.1). **Vector** length 68.1, 11.0% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.4 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[NG25 (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -4.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome assembly chaperone 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,658,043-12,728,945 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCCA3, MDS003, MGC15092, CLAST3, HsT1707, PAC2; previously TNFSF5IP1 |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969U7](https://www.uniprot.org/uniprotkb/Q969U7) (Proteasome assembly chaperone 2):

> Chaperone protein which promotes assembly of the 20S proteasome as part of a heterodimer with PSMG1. The PSMG1-PSMG2 heterodimer binds to the PSMA5 and PSMA7 proteasome subunits, promotes assembly of the proteasome alpha subunits into the heteroheptameric alpha ring and prevents alpha ring dimerization.

**Summary**, from NCBI Gene [56984](https://www.ncbi.nlm.nih.gov/gene/56984):

> Enables molecular adaptor activity. Involved in chaperone-mediated protein complex assembly and proteasome core complex assembly. Located in nucleus. Part of protein folding chaperone complex. Implicated in proteosome-associated autoinflammatory syndrome 4. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24929) · Entrez [56984](https://www.ncbi.nlm.nih.gov/gene/56984) · UniProt [Q969U7](https://www.uniprot.org/uniprotkb/Q969U7) · Ensembl [ENSG00000128789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128789)

## Data

Gene col 4920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4920); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4920]; `tensor/DDL_lfc|DDL_z.npy` [4920]; `embed/gene_vectors.npy` [4920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4920 or target_col == 4920). Every well: [[PSMG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
