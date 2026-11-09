---
symbol: "THSD4-AS1"
type: "gene"
col: 15250
ensembl_id: "ENSG00000259964"
name: "THSD4 antisense RNA 1"
location: "15q23"
module: 67
arm: "+"
pooled_cpm: 11.2
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# THSD4-AS1

*THSD4 antisense RNA 1* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.57× (z +10.3, q 3e-22, up in 32 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.71× (z +3.7, q 0.014, up in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 7.79×, PANC-1 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 6.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (PANC-1 4.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.795× (z -5.7, q 8e-06, down in 37 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.663× (z -4.2, q 0.009, down in 26 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.216×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGB1P5]] (+0.79, fdr 7e-06, ⚠ HMGB1P5 in the vector space only through flagged drug-doses), [[HMGB1]] (+0.77, fdr 7e-06), [[SPC25]] (+0.67, fdr 1e-05), [[CBX3]] (+0.67, fdr 2e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01515]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 7.79×, PANC-1 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 6.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (PANC-1 4.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **5.57×** | +10.3 | 3e-22 | 32/35 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **4.34×** | +10.1 | 1e-21 | 16/18 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.17×** | +7.7 | 3e-12 | 24/26 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.25×** | +5.9 | 7e-07 | 32/45 (SW480, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **2.16×** | +5.5 | 3e-06 | 29/38 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.5 | 5e-04 | 25/40 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.83×** | +4.2 | 0.002 | 28/40 (NCI-H1792, Hs 766T, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.014 | 23/46 (A-172, SW480, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.37×** | +3.3 | 0.071 | 23/48 (Panc 03.27, NCI-H23, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.090 | 17/47 (SW480, NCI-H23, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.216×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.795×** | -5.7 | 8e-06 | 37/48 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.663×** | -4.2 | 0.009 | 26/45 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.619× | -3.2 | 0.22 | 20/45 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.632× | -3.0 | 0.32 | 14/47 (HCT15, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.79× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.2) |
| [[A-172 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB1P5]] ⚠ | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[HMGB1]] | +0.77 | +0.84 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SPC25]] | +0.67 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[CBX3]] | +0.67 | +0.75 / +0.46 | both halves | 2e-05 |  |
| [[OIP5]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MELK]] | +0.64 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[SPC24]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[C9orf40]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[KIF15]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[BARD1]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[NUDT1]] | +0.62 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[KNL1]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CLSPN]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01515]] | B | LINC01515 activity lowers THSD4-AS1's level | lines that do not express LINC01515 (15) vs lines expressing it (35) | 1.29× higher at baseline in the lines without LINC01515 | 0.027 | ⚠ within organs, on part of the lines; also absent: DANT1 |
| [[MIR924HG]] | B | MIR924HG activity lowers THSD4-AS1's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.49× higher at baseline in the lines without MIR924HG | 0.045 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.0, -52.6); signed map (-47.0, -45.6). **Vector** length 52.0, 9.36% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 12); *G2/M checkpoint* (hallmark, mean cos +0.59 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +2.7 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | +2.1 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +3.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.1 | +1.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | -2.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | THSD4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q23 — chr15:71,147,650-71,189,064 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51420) · Entrez [101929196](https://www.ncbi.nlm.nih.gov/gene/101929196) · Ensembl [ENSG00000259964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259964)

## Data

Gene col 15250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15250); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15250]; `tensor/DDL_lfc|DDL_z.npy` [15250]; `embed/gene_vectors.npy` [15250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15250 or target_col == 15250). Every well: [[THSD4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THSD4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
