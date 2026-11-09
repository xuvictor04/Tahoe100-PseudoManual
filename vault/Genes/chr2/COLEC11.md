---
symbol: "COLEC11"
type: "gene"
col: 3959
ensembl_id: "ENSG00000118004"
name: "collectin subfamily member 11"
location: "2p25.3"
module: 21
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# COLEC11

*collectin subfamily member 11* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.61× (z +19.8, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Balsalazide (sodium hydrate) (drug)]] 5 µM: 0.652× (z -4.5, q 0.004, down in 13 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM184B]] (+0.79, fdr 7e-06), [[DENND6A-AS1]] (+0.79, fdr 7e-06), [[ABHD15-AS1]] (+0.74, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.61×** | +19.8 | 0e+00 | 33/33 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.82×** | +12.6 | 8e-34 | 21/29 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +11.1 | 2e-26 | 28/35 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.42×** | +10.6 | 4e-24 | 27/37 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.64×** | +10.2 | 2e-22 | 24/45 (A-172, SW1417, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **6.65×** | +7.4 | 2e-11 | 19/28 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **6.17×** | +7.1 | 1e-10 | 23/37 (LoVo, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +7.0 | 2e-10 | 1/2 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +6.9 | 3e-10 | 8/13 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +6.6 | 3e-09 | 6/15 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.86×** | +6.5 | 4e-09 | 9/46 (SW480, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +6.1 | 4e-08 | 23/46 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.87×** | +5.3 | 6e-06 | 0/4 | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.2 | 6e-06 | 9/21 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.2 | 7e-06 | 0/1 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.63×** | +5.1 | 1e-05 | 16/45 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +4.9 | 4e-05 | 11/42 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +4.7 | 9e-05 | 18/41 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +4.5 | 2e-04 | 7/31 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 6/45 (C32, HEC-1-A, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.003 | 12/45 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **0.652×** | -4.5 | 0.004 | 13/46 (A-172, HCT15, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.651× | -3.1 | 0.30 | 9/42 (C32, HOP62, …) | top dose only | position effect removed |
| [[Furosemide (drug)]] 5 µM |  | 0.747× | -3.1 | 0.30 | 11/46 (SHP-77, NCI-H1573, …) | top dose only | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | 0.749× | -3.0 | 0.30 | 5/45 (NCI-H1792, SNU-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -3.0 | 0.30 | 15/47 (J82, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.33 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 2.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +12.7) | — |
| [[A498 (line)]] | wt | 1.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.7× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 2.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.5× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 3.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.89× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 2.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 6.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 2.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 7.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM184B]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.79 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[ABHD15-AS1]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.74 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[MYLK3]] | +0.74 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.73 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.72 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[TOMM20L-DT]] | +0.72 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MGC4859]] | +0.71 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[H2AZ1-DT]] | +0.71 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[ESR2]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COLEC11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 23.2); signed map (29.3, 0.3). **Vector** length 53.5, 7.28% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +19.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | collectin subfamily member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:3,594,832-3,644,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3279, CL-K1, CL-11 |
| Gene groups (HGNC) | Collectins; C-type lectin domain containing; Complement system activation components |
| Reactome | 8 pathways, smallest: Lectin pathway of complement activation; Creation of C4 and C2 activators; Initial triggering of complement |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWP8](https://www.uniprot.org/uniprotkb/Q9BWP8) (Collectin-11):

> Lectin that plays a role in innate immunity, apoptosis and embryogenesis. Calcium-dependent lectin that binds self and non-self glycoproteins presenting high mannose oligosaccharides with at least one terminal alpha-1,2-linked mannose epitope. Primarily recognizes the terminal disaccharide of the glycan. Also recognizes a subset of fucosylated glycans and lipopolysaccharides. Plays a role in innate immunity through its ability to bind non-self sugars presented by microorganisms and to activate …

**Summary**, from NCBI Gene [78989](https://www.ncbi.nlm.nih.gov/gene/78989):

> This gene encodes a member of the collectin family of C-type lectins that possess collagen-like sequences and carbohydrate recognition domains. Collectins are secreted proteins that play important roles in the innate immune system by binding to carbohydrate antigens on microorganisms, facilitating their recognition and removal. The encoded protein binds to multiple sugars with a preference for fucose and mannose. Mutations in this gene are a cause of 3MC syndrome-2. Alternatively spliced …

**Accessions** — [HGNC:17213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17213) · Entrez [78989](https://www.ncbi.nlm.nih.gov/gene/78989) · UniProt [Q9BWP8](https://www.uniprot.org/uniprotkb/Q9BWP8) · Ensembl [ENSG00000118004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118004)

## Data

Gene col 3959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3959); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3959]; `tensor/DDL_lfc|DDL_z.npy` [3959]; `embed/gene_vectors.npy` [3959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3959 or target_col == 3959). Every well: [[COLEC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COLEC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
