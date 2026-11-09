---
symbol: "CCZ1"
type: "gene"
col: 4362
ensembl_id: "ENSG00000122674"
name: "CCZ1 vacuolar protein trafficking and biogenesis associated"
location: "7p22.1"
module: 30
arm: "+"
pooled_cpm: 23.32
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CCZ1

*CCZ1 vacuolar protein trafficking and biogenesis associated* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.39× (z +5.6, q 1e-05, up in 23 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.85× (z +5.5, q 1e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.694× (z -6.2, q 3e-07, down in 22 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.742× (z -5.1, q 1e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCZ1B]] (+0.97, fdr 7e-06), [[MALSU1]] (+0.73, fdr 7e-06), [[KLHDC10]] (+0.72, fdr 7e-06); moves opposite to [[LINC00641]] (-0.70, fdr 7e-06), [[PPP1R10]] (-0.67, fdr 7e-06), [[RNF32-AS1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[XKR8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.6 | 1e-05 | 23/47 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +5.5 | 1e-05 | 22/48 (PANC-1, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.2 | 3e-05 | 22/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +5.2 | 3e-05 | 25/48 (SW480, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.8 | 2e-04 | 20/47 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 18/47 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.006 | 18/48 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.025 | 12/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.20× | +3.1 | 0.13 | 6/47 (RPMI-7951, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.694×** | -6.2 | 3e-07 | 22/42 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.742×** | -5.1 | 1e-04 | 20/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -4.6 | 8e-04 | 23/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.786×** | -3.9 | 0.012 | 17/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.796×** | -3.6 | 0.038 | 15/37 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.3 | 0.089 | 20/47 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.830× | -3.2 | 0.13 | 4/48 (Panc 03.27, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.193× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 1 | — | [[Futibatinib (drug)]] 0.05 µM 0.203× (z -8.8) |
| [[HS-578T (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCZ1B]] | +0.97 | +0.94 / +0.94 | both halves | 7e-06 | pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 968 |
| [[MALSU1]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MMS19]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[FLYWCH2]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00641]] | -0.70 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[PPP1R10]] | -0.67 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | -0.66 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.66 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[THOC6]] | -0.65 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.64 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[CCDC200]] | -0.62 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MTNR1A]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[DDX5]] | -0.60 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR8]] | B | XKR8 activity lowers CCZ1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.43× higher at baseline in the lines without XKR8 | 0.089 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[HDAC6]] | B | HDAC6 activity lowers CCZ1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.6, -13.5); signed map (-37.2, 0.4). **Vector** length 82.5, 16.3% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +4.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | CCZ1 vacuolar protein trafficking and biogenesis associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,898,725-5,926,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-43, CCZ1A; previously C7orf28A |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P86791](https://www.uniprot.org/uniprotkb/P86791) (Vacuolar fusion protein CCZ1 homolog):

> Acts in concert with MON1A, as a guanine exchange factor (GEF) for RAB7, promotes the exchange of GDP to GTP, converting it from an inactive GDP-bound form into an active GTP-bound form.

**Summary**, from NCBI Gene [51622](https://www.ncbi.nlm.nih.gov/gene/51622):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in vacuolar transport and vesicle-mediated transport. Located in late endosome. Part of Mon1-Ccz1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21691) · Entrez [51622](https://www.ncbi.nlm.nih.gov/gene/51622) · UniProt [P86791](https://www.uniprot.org/uniprotkb/P86791) · Ensembl [ENSG00000122674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122674)

## Data

Gene col 4362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4362); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4362]; `tensor/DDL_lfc|DDL_z.npy` [4362]; `embed/gene_vectors.npy` [4362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4362 or target_col == 4362). Every well: [[CCZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
