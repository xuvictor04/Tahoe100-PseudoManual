---
symbol: "HSCB"
type: "gene"
col: 1890
ensembl_id: "ENSG00000100209"
name: "HscB mitochondrial iron-sulfur cluster cochaperone"
location: "22q12.1"
module: 114
arm: "+"
pooled_cpm: 22.52
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# HSCB

*HscB mitochondrial iron-sulfur cluster cochaperone* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +7.1, q 8e-10, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.580× (z -6.9, q 3e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF791]] (+0.72, fdr 7e-06), [[FBXO28]] (+0.69, fdr 7e-06), [[YJU2B]] (+0.64, fdr 1e-05); moves opposite to [[ACTB]] (-0.62, fdr 1e-05), [[ICMT]] (-0.58, fdr 2e-05), [[ATP5F1A]] (-0.57, fdr 2e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.1 | 8e-10 | 34/47 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 6e-04 | 24/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -6.9 | 3e-09 | 31/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -5.6 | 7e-06 | 29/45 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.1 | 8e-05 | 28/46 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.9 | 1e-04 | 27/45 (hTERT-HPNE, A-427, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -4.7 | 3e-04 | 28/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.780×** | -4.4 | 8e-04 | 26/47 (NCI-H1573, NCI-H1792, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -4.3 | 0.001 | 25/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.079 | 18/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.763×** | -3.2 | 0.080 | 18/47 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.081 | 14/48 (SNU-423, LoVo, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 0.787× | -3.0 | 0.13 | 13/48 (NCI-H460, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 56.6 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -14.2) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -9.1) |
| [[KATO III (line)]] | alt | 23.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.290× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0558× (z -16.2) ⚠ toxic · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.147× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.194× (z -9.9) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0520× (z -14.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -13.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H23 (line)]] | alt | 26.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0462× (z -10.9) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF791]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[FBXO28]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[EAPP]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ZSWIM3]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.63 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RNF181]] | +0.58 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[OFD1]] | +0.58 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[HELB]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PCF11-AS1]] | +0.58 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTB]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ICMT]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ATP5F1A]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 504 |
| [[MMGT1]] | -0.57 | -0.57 / -0.57 | both halves | 9e-06 | pathway: Protein localization |
| [[CS]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 543 |
| [[TFDP1]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RPSA]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 | pathway: Protein localization |
| [[CELSR2]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NONO]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[SORT1]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[FAM120A]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ERMP1]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HSCB's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.0, 4.3); signed map (-4.2, -11.3). **Vector** length 82.6, 17.1% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | HscB mitochondrial iron-sulfur cluster cochaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:28,742,039-28,757,515 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSC20, DNAJC20, Jac1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Reactome | 7 pathways, smallest: Mitochondrial iron-sulfur cluster biogenesis; Complex III assembly; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWL3](https://www.uniprot.org/uniprotkb/Q8IWL3) (Iron-sulfur cluster co-chaperone protein HscB):

> [Iron-sulfur cluster co-chaperone protein HscB, mitochondrial]: Acts as a co-chaperone in iron-sulfur cluster assembly in mitochondria. Required for incorporation of iron-sulfur clusters into SDHB, the iron-sulfur protein subunit of succinate dehydrogenase that is involved in complex II of the mitochondrial electron transport chain. Recruited to SDHB by interaction with SDHAF1 which first binds SDHB and then recruits the iron-sulfur transfer complex formed by HSC20, HSPA9 and ISCU through …

**Summary**, from NCBI Gene [150274](https://www.ncbi.nlm.nih.gov/gene/150274):

> This gene encodes a DnaJ-type co-chaperone and member of the heat shock cognate B (HscB) family of proteins. The encoded protein plays a role in the synthesis of iron-sulfur clusters, protein cofactors that are involved in the redox reactions of mitochondrial electron transport and other processes. Cells in which this gene is knocked down exhibit reduced activity of iron-sulfur cluster-dependent enzymes including succinate dehydrogenase and aconitase. The encoded protein may stimulate the …

**Accessions** — [HGNC:28913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28913) · Entrez [150274](https://www.ncbi.nlm.nih.gov/gene/150274) · UniProt [Q8IWL3](https://www.uniprot.org/uniprotkb/Q8IWL3) · Ensembl [ENSG00000100209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100209)

## Data

Gene col 1890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1890); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1890]; `tensor/DDL_lfc|DDL_z.npy` [1890]; `embed/gene_vectors.npy` [1890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1890 or target_col == 1890). Every well: [[HSCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
