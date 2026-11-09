---
symbol: "MIF"
type: "gene"
col: 14255
ensembl_id: "ENSG00000240972"
name: "macrophage migration inhibitory factor"
location: "22q11.23"
module: 48
arm: "+"
pooled_cpm: 195.18
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# MIF

*macrophage migration inhibitory factor* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.50× (z +4.9, q 7e-04, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.313× (z -8.6, q 4e-15, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFB11]] (+0.84, fdr 7e-06, ⚠ NDUFB11 in the vector space only through flagged drug-doses), [[UQCR11]] (+0.83, fdr 7e-06), [[ROMO1]] (+0.82, fdr 7e-06), [[COX7C]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.50×** | +4.9 | 7e-04 | 47/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.20×** | +4.4 | 0.003 | 44/49 (A498, PANC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.24×** | +4.1 | 0.006 | 37/44 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **2.17×** | +4.1 | 0.006 | 45/48 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.7 | 0.026 | 45/47 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.96×** | +3.3 | 0.091 | 32/45 (NCI-H2030, A498, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.313×** | -8.6 | 4e-15 | 48/48 (Panc 03.27, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -4.5 | 0.002 | 42/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.427×** | -4.5 | 0.002 | 46/48 (RKO, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.479×** | -3.9 | 0.016 | 45/48 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.287×** | -3.4 | 0.070 | 46/49 (C-33 A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.320× | -3.1 | 0.17 | 43/49 (BT-474, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.95 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 235 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.4) |
| [[AN3 CA (line)]] | alt | 197 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.1) |
| [[BT-474 (line)]] | alt | 169 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.2) |
| [[C-33 A (line)]] | alt | 167 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.4) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.3) |
| [[HCT15 (line)]] | alt | 241 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.5) |
| [[J82 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.6) |
| [[KATO III (line)]] | alt | 305 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.5) |
| [[LoVo (line)]] | wt | 230 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -8.9) |
| [[LS 180 (line)]] | wt | 267 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 269 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.4) |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 402 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.6) |
| [[RKO (line)]] | wt | 220 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 200 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.7) |
| [[SHP-77 (line)]] | alt | 192 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -11.8) |
| [[SW 1271 (line)]] | alt | 203 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -9.0) |
| [[SW 900 (line)]] | alt | 188 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -8.8) |
| [[SW48 (line)]] | wt | 202 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.6) |
| [[SW480 (line)]] | alt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.4) |
| [[A-172 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 266 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 250 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 352 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 207 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB11]] ⚠ | +0.84 | +0.78 / +0.81 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[UQCR11]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ROMO1]] | +0.82 | +0.76 / +0.85 | both halves | 7e-06 |  |
| [[COX7C]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[UQCRQ]] ⚠ | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6A1]] | +0.77 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.77 | +0.64 / +0.83 | both halves | 7e-06 |  |
| [[UBL5]] | +0.77 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[RPS29]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[NDUFA1]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[DPM3]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[MZT2B]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[COPS9]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MIF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.7, -22.0); signed map (-34.9, 9.6). **Vector** length 85.3, 52.7% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.68 to 31); *Respiratory electron transport* (reactome, mean cos +0.68 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.69 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +5.9 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | -0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -6.2 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +1.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | macrophage migration inhibitory factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,894,383-23,895,227 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GIF; previously GLIF |
| Gene groups (HGNC) | MIF family |
| Hallmark sets | FATTY_ACID_METABOLISM, GLYCOLYSIS, HYPOXIA |
| Reactome | 9 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P14174](https://www.uniprot.org/uniprotkb/P14174) (Macrophage migration inhibitory factor):

> Pro-inflammatory cytokine involved in the innate immune response to bacterial pathogens. The expression of MIF at sites of inflammation suggests a role as mediator in regulating the function of macrophages in host defense. Counteracts the anti-inflammatory activity of glucocorticoids. Has phenylpyruvate tautomerase and dopachrome tautomerase activity (in vitro), but the physiological substrate is not known. It is not clear whether the tautomerase activity has any physiological relevance, and …

**Summary**, from NCBI Gene [4282](https://www.ncbi.nlm.nih.gov/gene/4282):

> This gene encodes a lymphokine involved in cell-mediated immunity, immunoregulation, and inflammation. It plays a role in the regulation of macrophage function in host defense through the suppression of anti-inflammatory effects of glucocorticoids. This lymphokine and the JAB1 protein form a complex in the cytosol near the peripheral plasma membrane, which may indicate an additional role in integrin signaling pathways. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7097) · Entrez [4282](https://www.ncbi.nlm.nih.gov/gene/4282) · UniProt [P14174](https://www.uniprot.org/uniprotkb/P14174) · Ensembl [ENSG00000240972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240972)

## Data

Gene col 14255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14255); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14255]; `tensor/DDL_lfc|DDL_z.npy` [14255]; `embed/gene_vectors.npy` [14255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14255 or target_col == 14255). Every well: [[MIF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
