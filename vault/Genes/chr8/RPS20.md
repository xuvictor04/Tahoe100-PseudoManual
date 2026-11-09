---
symbol: "RPS20"
type: "gene"
col: 184
ensembl_id: "ENSG00000008988"
name: "ribosomal protein S20"
location: "8q12.1"
module: 43
arm: "+"
pooled_cpm: 215.23
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS20

*ribosomal protein S20* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.77× (z +8.8, q 6e-16, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +6.3, q 6e-08, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.714× (z -4.0, q 0.036, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.371×, C-33 A 0.417×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL12]] (+0.92, fdr 7e-06), [[RPL11]] (+0.92, fdr 7e-06), [[RPLP1]] (+0.92, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.73, fdr 7e-06), [[DCLRE1A]] (-0.66, fdr 7e-06), [[THOP1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +8.8 | 6e-16 | 49/49 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +8.7 | 1e-15 | 44/44 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +7.0 | 4e-10 | 44/45 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.3 | 6e-08 | 44/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.04×** | +6.0 | 2e-07 | 48/48 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.1 | 0.004 | 43/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.004 | 36/50 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.56×** | +3.6 | 0.022 | 32/47 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.48×** | +3.3 | 0.057 | 43/48 (SHP-77, HT-29, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.087 | 33/48 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.45×** | +3.1 | 0.087 | 39/48 (NCI-H460, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.371×, C-33 A 0.417×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.714×** | -4.0 | 0.036 | 34/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 213 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.8) |
| [[LoVo (line)]] | wt | 371 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 169 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 202 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.8) |
| [[A498 (line)]] | wt | 291 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 205 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 267 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 208 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +9.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 232 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 223 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 234 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 231 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 267 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 208 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 229 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 198 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 264 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 195 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 359 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 368 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL12]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.92 | +0.93 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.92 | +0.88 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS4X]] | +0.91 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL30]] ⚠ | +0.91 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.90 | +0.88 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS12]] | +0.90 | +0.86 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL13A]] | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.89 | +0.86 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.73 | -0.64 / -0.73 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[THOP1]] | -0.65 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[MIS12]] | -0.65 | -0.57 / -0.63 | both halves | 9e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.920). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.8, -29.2); signed map (-60.5, -5.8). **Vector** length 89.9, 49.7% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.85 to 34); *MYC targets v1* (hallmark, mean cos +0.68 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.61 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.4 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:56,067,254-56,074,510 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S20, uS10 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P60866](https://www.uniprot.org/uniprotkb/P60866) (Small ribosomal subunit protein uS10):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6224](https://www.ncbi.nlm.nih.gov/gene/6224):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S10P family of ribosomal proteins. It is located in the cytoplasm. This gene is co-transcribed with the small nucleolar RNA gene U54, which is located in its second intron. …

**Accessions** — [HGNC:10405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10405) · Entrez [6224](https://www.ncbi.nlm.nih.gov/gene/6224) · UniProt [P60866](https://www.uniprot.org/uniprotkb/P60866) · Ensembl [ENSG00000008988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008988)

## Data

Gene col 184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 184); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 184]; `tensor/DDL_lfc|DDL_z.npy` [184]; `embed/gene_vectors.npy` [184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 184 or target_col == 184). Every well: [[RPS20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
