---
symbol: "RPS5"
type: "gene"
col: 1385
ensembl_id: "ENSG00000083845"
name: "ribosomal protein S5"
location: "19q13.43"
module: 43
arm: "+"
pooled_cpm: 209.59
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS5

*ribosomal protein S5* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.07× (z +6.7, q 1e-08, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -6.1, q 8e-07, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.317×, C-33 A 0.334×, RKO 0.358×, H4 0.309×, …); [[Everolimus (drug)]] 5 µM in 1 line (NCI-H596 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS25]] (+0.93, fdr 7e-06), [[RPL32]] (+0.93, fdr 7e-06), [[RPL11]] (+0.92, fdr 7e-06); moves opposite to [[PSME3IP1]] (-0.69, fdr 1e-05), [[SEPTIN8]] (-0.66, fdr 1e-05), [[MIS12]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1385.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.07×** | +6.7 | 1e-08 | 48/49 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.57×** | +6.0 | 5e-07 | 41/44 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.12×** | +4.6 | 8e-04 | 41/45 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.91×** | +4.3 | 0.003 | 43/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.87×** | +4.1 | 0.004 | 48/48 (COLO 205, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.8 | 0.014 | 42/47 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.75×** | +3.7 | 0.018 | 45/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.66×** | +3.4 | 0.054 | 39/48 (COLO 205, NCI-H460, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.62×** | +3.2 | 0.085 | 40/48 (COLO 205, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 1.61× | +3.0 | 0.14 | 37/47 (A-172, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1385.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.317×, C-33 A 0.334×, RKO 0.358×, H4 0.309×, …); [[Everolimus (drug)]] 5 µM in 1 line (NCI-H596 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -6.1 | 8e-07 | 42/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 202 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.1) |
| [[C-33 A (line)]] | alt | 284 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.8) |
| [[CHP-212 (line)]] | wt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.8) |
| [[COLO 205 (line)]] | alt | 68.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 211 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -8.9) |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 1 | — | [[Everolimus (drug)]] 5 µM 0.130× (z -8.6) |
| [[RKO (line)]] | wt | 259 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.0) |
| [[A-172 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 283 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 275 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 218 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 261 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 223 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 213 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 369 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 273 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 239 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS25]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL32]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP0]] | +0.91 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPS16]] ⚠ | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RACK1]] | +0.90 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPS14]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL7A]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27]] | +0.89 | +0.85 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.89 | +0.87 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.89 | +0.88 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.88 | +0.88 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | -0.69 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SEPTIN8]] | -0.66 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MIS12]] | -0.66 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.65 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[SCAF1]] | -0.64 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RPS5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.895). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.8, -28.5); signed map (-61.3, -4.8). **Vector** length 90.8, 53.1% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.82 to 34); *oxidative phosphorylation* (hallmark, mean cos +0.64 to 9); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.62 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.9 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.6 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.5 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.2 | +0.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +1.9 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -6.6 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -6.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.1 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -0.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.7 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,386,400-58,394,806 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S5, uS7 |
| Gene groups (HGNC) | S ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P46782](https://www.uniprot.org/uniprotkb/P46782) (Small ribosomal subunit protein uS7):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6193](https://www.ncbi.nlm.nih.gov/gene/6193):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S7P family of ribosomal proteins. It is located in the cytoplasm. Variable expression of this gene in colorectal cancers compared to adjacent normal tissues has been …

**Accessions** — [HGNC:10426](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10426) · Entrez [6193](https://www.ncbi.nlm.nih.gov/gene/6193) · UniProt [P46782](https://www.uniprot.org/uniprotkb/P46782) · Ensembl [ENSG00000083845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083845)

## Data

Gene col 1385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1385); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1385]; `tensor/DDL_lfc|DDL_z.npy` [1385]; `embed/gene_vectors.npy` [1385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1385 or target_col == 1385). Every well: [[RPS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
