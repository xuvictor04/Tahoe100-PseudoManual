---
symbol: "OST4"
type: "gene"
col: 13649
ensembl_id: "ENSG00000228474"
name: "oligosaccharyltransferase complex subunit 4, non-catalytic"
location: "2p23.3"
module: 48
arm: "+"
pooled_cpm: 35.08
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# OST4

*oligosaccharyltransferase complex subunit 4, non-catalytic* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.22× (z +6.7, q 1e-08, up in 41 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +6.5, q 2e-08, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -6.0, q 1e-06, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.200×, RPMI-7951 0.226×, NCI-H2030 0.327×, A-427 0.336×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSR4]] (+0.85, fdr 7e-06), [[RABAC1]] (+0.81, fdr 7e-06), [[NDUFA2]] (+0.81, fdr 1e-05); moves opposite to [[SFPQ]] (-0.66, fdr 1e-05), [[PSMG1]] (-0.64, fdr 7e-06), [[COA7]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR4458HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.22×** | +6.7 | 1e-08 | 41/44 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.5 | 2e-08 | 46/48 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.48×** | +6.1 | 2e-07 | 31/36 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.05×** | +4.8 | 2e-04 | 30/39 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.82×** | +4.4 | 0.002 | 35/47 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | 1.59× | +3.2 | 0.15 | 32/48 (HT-29, SNU-423, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.58× | +3.1 | 0.15 | 25/47 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13649.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.200×, RPMI-7951 0.226×, NCI-H2030 0.327×, A-427 0.336×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -6.0 | 1e-06 | 38/47 (RKO, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 0.630× | -3.4 | 0.22 | 31/48 (A-172, SW 900, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.442× | -3.1 | 0.29 | 33/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.642× | -3.0 | 0.29 | 28/47 (C32, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 57.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 75.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.5) |
| [[RKO (line)]] | wt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.4) |
| [[A-172 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSR4]] | +0.85 | +0.80 / +0.85 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 904 |
| [[RABAC1]] | +0.81 | +0.64 / +0.87 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.81 | +0.54 / +0.84 | both halves | 1e-05 |  |
| [[UBL5]] | +0.78 | +0.64 / +0.84 | both halves | 7e-06 |  |
| [[DDT]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[ZNHIT1]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[SERF2]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[UQCRQ]] ⚠ | +0.74 | +0.64 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[FAU]] | +0.72 | +0.61 / +0.75 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[ATP5MK]] | +0.72 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[MIF]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[ATP5PD]] | +0.71 | +0.48 / +0.75 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.66 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[COA7]] | -0.64 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[PIGO]] | -0.64 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[POGK]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[N6AMT1]] | -0.62 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[BACE1-AS]] | -0.61 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[DHX9]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[AGPS]] | -0.61 | -0.40 / -0.74 | both halves | 5e-05 | pathway: Protein localization |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4458HG]] | B | MIR4458HG activity lowers OST4's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.38× higher at baseline in the lines without MIR4458HG | 0.043 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.7, -21.4); signed map (-34.1, 10.6). **Vector** length 70.0, 23.2% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.61 to 31); *Respiratory electron transport* (reactome, mean cos +0.61 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.63 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +2.9 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.05 µM |  | +1.0 | +1.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -3.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.6 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | oligosaccharyltransferase complex subunit 4, non-catalytic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,070,472-27,071,654 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C6T2](https://www.uniprot.org/uniprotkb/P0C6T2) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit 4):

> Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates protein …

**Summary**, from NCBI Gene [100128731](https://www.ncbi.nlm.nih.gov/gene/100128731):

> Involved in protein N-linked glycosylation. Part of oligosaccharyltransferase complex A and oligosaccharyltransferase complex B. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32483) · Entrez [100128731](https://www.ncbi.nlm.nih.gov/gene/100128731) · UniProt [P0C6T2](https://www.uniprot.org/uniprotkb/P0C6T2) · Ensembl [ENSG00000228474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228474)

## Data

Gene col 13649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13649); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13649]; `tensor/DDL_lfc|DDL_z.npy` [13649]; `embed/gene_vectors.npy` [13649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13649 or target_col == 13649). Every well: [[OST4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OST4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
