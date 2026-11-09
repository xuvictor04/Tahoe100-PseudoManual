---
symbol: "RNF32"
type: "gene"
col: 2698
ensembl_id: "ENSG00000105982"
name: "ring finger protein 32"
location: "7q36.3"
module: 10
arm: "+"
pooled_cpm: 5.06
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RNF32

*ring finger protein 32* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.22× (z +13.0, q 4e-36, up in 23 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +8.7, q 5e-16, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.473× (z -8.4, q 3e-14, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCL3P4]] (+0.73, fdr 1e-05), [[GRK4]] (+0.72, fdr 1e-05), [[TMEM9B-AS1]] (+0.72, fdr 9e-05); moves opposite to [[L2HGDH]] (-0.67, fdr 4e-05), [[KLHL8]] (-0.62, fdr 1e-04), [[CCDC134]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RNF32-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +13.0 | 4e-36 | 23/25 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +12.9 | 2e-35 | 6/6 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +9.5 | 2e-19 | 11/14 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.7 | 5e-16 | 24/40 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.004 | 9/36 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.028 | 5/40 (RKO, A-172, …) | inconsistent across doses | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.080 | 3/44 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.084 | 5/45 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.2 | 0.088 | 4/28 (A-427, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.088 | 8/43 (A-427, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.088 | 6/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.097 | 6/38 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -8.4 | 3e-14 | 24/42 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.605×** | -5.6 | 5e-06 | 24/47 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -5.2 | 4e-05 | 22/42 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -4.3 | 0.003 | 19/45 (SK-MEL-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -3.9 | 0.009 | 15/47 (Hs 766T, BT-474, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.049 | 7/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.597× | -3.0 | 0.21 | 12/44 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 5.34 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 0.5 µM 0.0625× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0666× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 3.51 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0612× (z -8.5) |
| [[PANC-1 (line)]] | alt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.7) | — |
| [[RKO (line)]] | wt | 9.50 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~85% of this change |
| [[A-172 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCL3P4]] | +0.73 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[GRK4]] | +0.72 | +0.79 / +0.50 | both halves | 1e-05 |  |
| [[TMEM9B-AS1]] | +0.72 | +0.84 / +0.37 | both halves | 9e-05 |  |
| [[USP38-DT]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[RAP2C-AS1]] | +0.71 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[DLGAP4-AS1]] | +0.70 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.69 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[F8]] | +0.69 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD31]] | +0.68 | +0.76 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.67 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[KLHL8]] | -0.62 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[CCDC134]] | -0.59 | -0.55 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF32-DT]] | B | RNF32-DT activity raises RNF32's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without RNF32-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RNF32's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises RNF32's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.35× lower at baseline in the lines without ANKRD20A21P | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.8, 18.6); signed map (31.6, -10.9). **Vector** length 47.4, 5.47% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:156,640,281-156,677,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG33, HSD15, LMBR2 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0A6](https://www.uniprot.org/uniprotkb/Q9H0A6) (RING finger protein 32):

> May play a role in sperm formation.

**Summary**, from NCBI Gene [140545](https://www.ncbi.nlm.nih.gov/gene/140545):

> The protein encoded by this gene contains two RING ring finger motifs. RING finger motifs are present in a variety of functionally distinct proteins and are known to be involved in protein-DNA or protein-protein interactions. This gene was found to be expressed during spermatogenesis, most likely in spermatocytes and/or in spermatids. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:17118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17118) · Entrez [140545](https://www.ncbi.nlm.nih.gov/gene/140545) · UniProt [Q9H0A6](https://www.uniprot.org/uniprotkb/Q9H0A6) · Ensembl [ENSG00000105982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105982)

## Data

Gene col 2698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2698); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2698]; `tensor/DDL_lfc|DDL_z.npy` [2698]; `embed/gene_vectors.npy` [2698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2698 or target_col == 2698). Every well: [[RNF32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
