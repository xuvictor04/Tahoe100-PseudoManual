---
symbol: "ZNHIT1"
type: "gene"
col: 2757
ensembl_id: "ENSG00000106400"
name: "zinc finger HIT-type containing 1"
location: "7q22.1"
module: 48
arm: "+"
pooled_cpm: 35.33
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ZNHIT1

*zinc finger HIT-type containing 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +9.4, q 4e-18, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.607× (z -4.5, q 0.005, down in 37 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.726× (z -3.8, q 0.049, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OST4]] (+0.77, fdr 7e-06), [[NDUFA2]] (+0.77, fdr 8e-06), [[RABAC1]] (+0.73, fdr 7e-06); moves opposite to [[RAD51D]] (-0.68, fdr 1e-05), [[DHX9]] (-0.67, fdr 7e-06), [[SFPQ]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +9.4 | 4e-18 | 45/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.32×** | +7.0 | 8e-10 | 38/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.01×** | +6.0 | 4e-07 | 23/37 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.79×** | +5.2 | 3e-05 | 42/48 (PANC-1, C-33 A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.66×** | +4.5 | 8e-04 | 34/48 (NCI-H460, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.2 | 0.003 | 35/45 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.55×** | +3.9 | 0.008 | 34/46 (CFPAC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.030 | 26/48 (C32, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.52×** | +3.5 | 0.030 | 25/41 (SHP-77, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.50×** | +3.5 | 0.030 | 24/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.035 | 28/48 (C-33 A, C32, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.45×** | +3.3 | 0.043 | 27/48 (PANC-1, C32, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +3.2 | 0.057 | 26/48 (HOP62, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.058 | 24/48 (HOP62, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.607×** | -4.5 | 0.005 | 37/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.726×** | -3.8 | 0.049 | 29/47 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 44.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 42.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.1) | — |
| [[KATO III (line)]] | alt | 59.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.2) | — |
| [[SW480 (line)]] | alt | 44.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.3) | — |
| [[A-172 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OST4]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.77 | +0.58 / +0.74 | both halves | 8e-06 |  |
| [[RABAC1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[SSR4]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[ATP5PF]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[UBL5]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[HINFP]] | +0.69 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[IFT20]] | +0.69 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[NARF]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SUPT4H1]] | +0.68 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[COMMD6]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD51D]] | -0.68 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[DHX9]] | -0.67 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.67 | -0.46 / -0.69 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.66 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ATIC]] | -0.66 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[FKTN]] | -0.66 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[POGK]] | -0.65 | -0.62 / -0.57 | both halves | 8e-06 |  |
| [[COA7]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.64 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.64 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PRRC2A]] | -0.63 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[DCLRE1A]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNHIT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[APOE]] | B | APOE activity raises ZNHIT1's level | lines that do not express APOE (25) vs lines expressing it (25) | 1.03× lower at baseline in the lines without APOE | 0.098 | ⚠ within organs, on part of the lines; also absent: SYT11, RNF175, GRIA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.4, -21.4); signed map (-33.8, 10.9). **Vector** length 67.7, 18.6% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.52 to 31); *Respiratory electron transport* (reactome, mean cos +0.52 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.53 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -0.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.0 | +1.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -3.3 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -3.2 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger HIT-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,218,165-101,224,190 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CG1I, H_DJ0747G18.14, p18(Hamlet); previously ZNFN4A1 |
| Gene groups (HGNC) | Zinc fingers HIT-type; SRCAP complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O43257](https://www.uniprot.org/uniprotkb/O43257) (Zinc finger HIT domain-containing protein 1):

> Plays a role in chromatin remodeling by promoting the incorporation of histone variant H2AZ1/H2A.Z into the genome to regulate gene expression. Promotes SRCAP complex-mediated deposition of histone variant H2AZ1 to lymphoid fate regulator genes, enhancing lymphoid lineage commitment (By similarity). Recruited to the promoter of the transcriptional activator MYOG at the early stages of muscle differentiation where it mediates binding of histone H2AZ1 to chromatin and induces muscle-specific gene …

**Summary**, from NCBI Gene [10467](https://www.ncbi.nlm.nih.gov/gene/10467):

> Enables histone binding activity. Involved in muscle cell differentiation and positive regulation of DNA damage response, signal transduction by p53 class mediator. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21688) · Entrez [10467](https://www.ncbi.nlm.nih.gov/gene/10467) · UniProt [O43257](https://www.uniprot.org/uniprotkb/O43257) · Ensembl [ENSG00000106400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106400)

## Data

Gene col 2757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2757); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2757]; `tensor/DDL_lfc|DDL_z.npy` [2757]; `embed/gene_vectors.npy` [2757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2757 or target_col == 2757). Every well: [[ZNHIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNHIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
